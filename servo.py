import time                #Importamos time para poder usar time.sleep
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO

GPIO.setmode(GPIO.BOARD)     #Ponemos la Raspberry en modo BOARD
SERVO = 35
GPIO.setup(SERVO, GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(SERVO, 50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(7.5)                   #Enviamos un pulso del 7.5% para centrar el servo

try:                 
    while True:      #iniciamos un loop infinito

        p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
        time.sleep(0.5)           #pausa de medio segundo

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo 
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

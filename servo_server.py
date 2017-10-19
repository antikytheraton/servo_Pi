# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
servo = 35
GPIO.setup(servo, GPIO.OUT)
p = GPIO.PWM(servo, 50)
p.start(7.5)

@app.route('/')
def hello():
    return 'Seismic-safe'

@app.route('/gasSystem/<option>', methods=['POST'])
def gasSystem(option):
    '''
    EndPoint sistema de gas
    '''
    if option == 'abrir':
        p.ChangeDutyCycle(4.5)
        p.stop()
        return '{0} sistema de gas'.format(option)
    elif option == 'cerrar':
        p.ChangeDutyCycle(10.5)
        p.stop()
        return '{0} sistema de gas'.format(option)
    else:
        return "Opcion invalida, opciones validas son 'abrir' o 'cerrar"

@app.route('/servo_test', methods=['POST'])
def servo_test():
    '''
    Prueba servo
    '''
    try:
        # while True:      #iniciamos un loop infinito

        p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
        time.sleep(0.5)           #pausa de medio segundo
        p.stop()                      #Detenemos el servo
        GPIO.cleanup()
        return 'test OK'

    except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
        p.stop()                      #Detenemos el servo
        GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )

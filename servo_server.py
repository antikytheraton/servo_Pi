# -*- coding: utf-8 -*-

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

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )

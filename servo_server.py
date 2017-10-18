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
    print(option)
    return '{0} sistema de gas'.format(option)

@app.route('/openGas', methods=['POST'])
def openGas():
    '''
    Endpoint apertura de paso de gas
    '''
    p.ChangeDutyCycle(4.5)
    print('Abriendo paso de gas')
    return 'Arbiendo paso de gas'

@app.route('/closeGas', methods=['POST'])
def closeGas():
    '''
    Endpoint cerrado de gas
    '''
    p.ChangeDutyCycle(10.5)
    print('Cerrando paso de gas')
    return 'Cerrando paso de gas'

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )

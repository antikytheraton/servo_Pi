import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
servo = 35
GPIO.setup(servo, GPIO.OUT)
p = GPIO.PWM(servo, 50)
p.start(7.5)

@app.route('/')
def hello(request):
    print(request)
    return 'hello'

@app.route('/openGas', methods=['POST'])
def openGas():
    p.ChangeDutyCycle(4.5)
    print('Abriendo paso de gas')

@app.route('/closeGas', methods=['POST'])
def closeGas():
    p.ChangeDutyCycle(10.5)
    print('Cerrando paso de gas')

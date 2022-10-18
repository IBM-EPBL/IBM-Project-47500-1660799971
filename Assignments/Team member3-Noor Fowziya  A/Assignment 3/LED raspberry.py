import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

led = 5

GPIO.setup(led, GPIO.OUT, initial = 0) 

while(True):

 GPIO.output(led, GPIO.HIGH) 

 time.sleep(2)

 

 GPIO.output(led, GPIO.LOW) 

 time.sleep(2)

   
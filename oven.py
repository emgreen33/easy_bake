import RPi.GPIO as gpio
from datetime import datetime

gpio.setmode(gpio.BOARD)
switch = 10

gpio.setup(switch, gpio.OUT, initial=False)

def on:
  gpio.output(switch, True)
  print "Oven switched ON at " + str(datetime.now())

def off:
  gpio.output(switch, False)
  print "Oven switched OFF at " + str(datetime.now())

def status:
  return gpio.input(switch)





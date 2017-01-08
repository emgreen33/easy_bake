import RPi.GPIO as gpio
from datetime import datetime
import time
import controller

gpio.setmode(gpio.BOARD)
switch = 10

gpio.setup(switch, gpio.OUT, initial=False)

def switch_on():
  gpio.output(switch, True)
  print "Oven switched ON at " + str(datetime.now())


def switch_off():
  gpio.output(switch, False)
  print "Oven switched OFF at " + str(datetime.now())

def status():
  return gpio.input(switch)

while True:
  switch_on()
  status()
  time.sleep(600)
  switch_off()
  status()
  break


gpio.cleanup()




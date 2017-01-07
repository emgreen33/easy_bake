import RPi.GPIO as gpio
import time

#use board numbering on the pi

gpio.setmode(gpio.BOARD)

gpio.setup(40, gpio.OUT)
gpio.setup(38, gpio.OUT)

#true and 1 are the same
gpio.output(40, True)
gpio.output(38, 1)

while True:
  gpio.output(40, True)
  gpio.output(38, False)
  time.sleep(250)
  gpio.output(40, 0)
  gpio.output(38, 1)


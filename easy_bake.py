import RPi.GPIO as gpio

#use board numbering on the pi

gpio.setmode(gpio.BOARD)

gpio.setup(40, gpio.OUT)
gpio.setup(38, gpio.IN)

#true and 1 are the same
gpio.output(40, True)
gpio.output(38, 1)

while True:
  gpio.output(40, True)
  gpio.output(38, False)
  sleep(250)
  gpio.output(40, 0)
  gpio.output(38, 1)


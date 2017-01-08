# import RPi.GPIO as gpio
# import time

# #use board numbering on the pi

# gpio.setmode(gpio.BOARD)
# # output_pins = [40, 38]
# output_pins = 16

# gpio.setup(output_pins, gpio.OUT)

# #true and 1 are the same
# # gpio.output(40, True)
# # gpio.output(38, 1)

# while True:
#   gpio.output(output_pins, (True, False))
# #   # gpio.output(40, True)
# #   # gpio.output(38, False)
#   time.sleep(1)
# #   # gpio.output(40, False)
# #   # gpio.output(38, True)
#   gpio.output(output_pins, (False, True))
#   time.sleep(1)

#   gpio.cleanup()



import RPi.GPIO as gpio
import time

#use board numbering on the pi

gpio.setmode(gpio.BOARD)
output_pins = [40, 38, 10]

gpio.setup(output_pins, gpio.OUT)

#true and 1 are the same
# gpio.output(40, True)
# gpio.output(38, 1)

while True:
  gpio.output(output_pins, (True, False, False))
  # gpio.output(40, True)
  # gpio.output(38, False)
  time.sleep(2)
  # gpio.output(40, False)
  # gpio.output(38, True)
  gpio.output(output_pins, (False, True, True))
  time.sleep(2)


gpio.cleanup()




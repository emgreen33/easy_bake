import oven
import time

while True:
  print oven.status()
  oven.switch_on()
  print oven.status()
  time.sleep(2)
  oven.switch_off()
  print oven.status()
  time.sleep(2)


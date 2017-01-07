import oven
import time

while True:
  print oven.status
  oven.on
  print oven.status
  time.sleep(2)
  oven.off
  print oven.status
  time.sleep(2)


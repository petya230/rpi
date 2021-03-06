#!/usr/bin/env python

import max7219.led as led
import max7219.font as font
import sys
import time
import fileinput

device = led.matrix(cascaded=8)
device.orientation(90)
device.brightness(3)

if len(sys.argv) == 1:
  for line in sys.stdin:
    #device.clear()
    device.show_message(line.rstrip('\n'), delay=.004)
  sys.exit(0)
print sys.argv
for word in sys.argv[1:]:
  device.show_message(word, delay=1)
  time.sleep(.5)
  

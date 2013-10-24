#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

SLEEP_TIME = 1

GPIO.setmode(GPIO.BCM)
GREEN_LED = 7

GPIO.setup(GREEN_LED, GPIO.OUT)

try:

  while True:
    print "Green light ON"
    GPIO.output(GREEN_LED, True)
    time.sleep(SLEEP_TIME)
    print "...OFF"
    GPIO.output(GREEN_LED, False)
    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
  GPIO.cleanup()

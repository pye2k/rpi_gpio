#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

SLEEP_TIME = 1

GPIO.setmode(GPIO.BCM)
GREEN_LED = 7
RED_LED = 8

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

try:

  while True:
    print "Green light ON"
    GPIO.output(GREEN_LED, True)
    time.sleep(SLEEP_TIME)
    print "Red light ON"
    GPIO.output(RED_LED, True)
    time.sleep(SLEEP_TIME)
    print "...ALL OFF"
    GPIO.output(GREEN_LED, False)
    GPIO.output(RED_LED, False)
    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
  GPIO.cleanup()

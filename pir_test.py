#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os

SLEEP_TIME = 0.5

GPIO.setmode(GPIO.BCM)

PIR_PIN = 18
GREEN_LED = 7
RED_LED = 8

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

try:

  while True:
    if GPIO.input(PIR_PIN):
      GPIO.output(GREEN_LED, True)
      print("Motion detected!!!")
    else:
      GPIO.output(GREEN_LED, False)

    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
  GPIO.cleanup()

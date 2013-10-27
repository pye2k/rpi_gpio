#!/usr/bin/env python

import wiringpi, time, os

SLEEP_TIME = 1

wiringpi.wiringPiSetupSys()

GREEN_LED = 7
RED_LED = 8

wiringpi.pinMode(GREEN_LED, wiringpi.OUTPUT)
wiringpi.pinMode(RED_LED, wiringpi.OUTPUT)

try:

  while True:
    print "Green light ON"
    wiringpi.digitalWrite(GREEN_LED, wiringpi.HIGH)
    time.sleep(SLEEP_TIME)
    print "Red light ON"
    wiringpi.digitalWrite(RED_LED, wiringpi.HIGH)
    time.sleep(SLEEP_TIME)
    print "...ALL OFF"
    wiringpi.digitalWrite(GREEN_LED, wiringpi.LOW)
    wiringpi.digitalWrite(RED_LED, wiringpi.LOW)
    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
  wiringpi.digitalWrite(GREEN_LED, wiringpi.LOW)
  wiringpi.digitalWrite(RED_LED, wiringpi.LOW)

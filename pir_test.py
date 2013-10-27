#!/usr/bin/env python

import wiringpi, time, os

SLEEP_TIME = 1

wiringpi.wiringPiSetupSys()

PIR_PIN = 18
GREEN_LED = 7
RED_LED = 8

wiringpi.pinMode(PIR_PIN, wiringpi.INPUT)
wiringpi.pinMode(GREEN_LED, wiringpi.OUTPUT)
wiringpi.pinMode(RED_LED, wiringpi.OUTPUT)

try:

  while True:
    if wiringpi.digitalRead(PIR_PIN):
      wiringpi.digitalWrite(GREEN_LED, wiringpi.HIGH)
      print("Motion detected!!!")
    else:
      wiringpi.digitalWrite(GREEN_LED, wiringpi.LOW)
      print("All quiet...")

    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
  wiringpi.digitalWrite(GREEN_LED, wiringpi.LOW)

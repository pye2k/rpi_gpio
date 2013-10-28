#!/usr/bin/python
'''
Created on 10/27/2013

@author: Alan Wong

Motion Detection - detects motion via PIR module onboard the Raspberry Pi; and emails when it does.
'''

import smtplib
from datetime import datetime, timedelta

import os.path
import sys
import ConfigParser

import wiringpi
import time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class PIRMotionDetection:

    def __init__(self, cfg_path):
        # Load config
        config = ConfigParser.ConfigParser()
        config.read(cfg_path)
        
        # GMail account credentials
        self.username = config.get('gmail', 'user')
        self.password = config.get('gmail', 'password')
        self.sender = config.get('gmail', 'sender')
        
        # Recipient email address (could be same as from_addr)
        self.recipients = config.get('gmail', 'recipients').split(',')
        
        # Subject line for email
        self.subject = config.get('gmail', 'subject')
        
        # First line of email message
        self.message = config.get('gmail', 'message')

    def _send_email(self,msg):
        '''Send an email using the GMail account.'''
        senddate=datetime.strftime(datetime.now(), '%Y-%m-%d')

        m = MIMEMultipart()
        m['From'] = self.sender
        m['To'] = ', '.join(self.recipients)
        m['Date'] = senddate
        m['Subject'] = self.subject
        
        m.attach( MIMEText(msg) )

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.sender, self.recipients, m.as_string())
        server.quit()

    def run(self):
        motionFirstDetectedTime = None
        SLEEP_TIME = 0.5

        # Set up the GPIO input for motion detection
        PIR_PIN = 18
        wiringpi.wiringPiSetupSys()
        wiringpi.pinMode(PIR_PIN, wiringpi.INPUT)

        # Loop through and detect motion
        while True:
            if wiringpi.digitalRead(PIR_PIN):
                if motionFirstDetectedTime is None:
                    motionFirstDetectedTime = datetime.now()
                    print('Motion detected at: ' + str(motionFirstDetectedTime))

            # Do we need to send out a notification?
            now = datetime.now()
            if (motionFirstDetectedTime is not None) and (now - motionFirstDetectedTime) > timedelta (minutes = 1):
                print('Sending out notification now!')
                motiondate = datetime.strftime(motionFirstDetectedTime, '%Y-%m-%d %H:%M:%S')
                msg = self.message + ': ' + motiondate 
                self._send_email(msg)

                # reset state
                motionFirstDetectedTime = None

            time.sleep(SLEEP_TIME)
            
if __name__ == '__main__':         
    try:
        if len(sys.argv) < 2:
            exit('Usage: pir_detect_motion.py {config-file-path}')
        cfg_path = sys.argv[1]
        if not os.path.exists(cfg_path):
            exit('Config file does not exist [%s]' % cfg_path)
        PIRMotionDetection(cfg_path).run()
    except Exception as e:
        exit('Error: [%s]' % e)

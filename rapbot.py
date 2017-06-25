#!/usr/bin/env python3
import configparser
import os
import sys
import time

try:
    import RPi.GPIO as GPIO
except:
    pass

from rapbot import main


config = configparser.ConfigParser()
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

config.read(os.path.join(ROOT_DIR, 'rapbot.conf'))

rpi = config['rapbot']['raspberry_pi']

if __name__ == '__main__':
    if rpi == 'True':
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        while True:
            input_state = GPIO.input(18)
            if input_state == False:
                main()
                time.sleep(0.2)
    else:
        main()

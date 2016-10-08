#!/usr/bin/python

import atexit
import dweepy
import signal
import sys
import time

import pyupm_grove as grove
import pyupm_grovespeaker as upmGrovespeaker
import pyupm_i2clcd as lcd


display = lcd.Jhd1313m1(0, 0x3E, 0x62)
light = grove.GroveLight(0)


def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':


    while True:

        luxes = light.value()
        luxes = int(luxes)
        luxes str(luxes)
        #display.setColor(luxes, luxes, luxes)
        #display.clear()
        display.setColor(0, 0, 0)
            
        display.setCursor(0,0)
        display.write(luxes)
        time.sleep(1)
        #display.clear()

       


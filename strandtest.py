# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
from time import sleep
from neopixel import *

import argparse
import signal
import sys
def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 15     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

chunkbrightness = 15


def colorWipe(strip, color, wait_ms=1):
	for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def xboxchunk(strip, color, wait_ms=1):
	for i in range(strip.numPixels()):
            if i == 0:
            
		strip.setPixelColor(12, Color(0, 0, 0))
		strip.setPixelColor(13, Color(0, 0, 0))
		strip.setPixelColor(14, Color(0, 0, 0))
		strip.setPixelColor(15, Color(0, 0, 0))

                strip.show() #flush LEDs (turn all off) 

                print("flush all")
                bright = 15
                for ii in range (0, 4):
                    strip.setPixelColor(0, color)
		    strip.setPixelColor(1, color)
		    strip.setPixelColor(2, color)
		    strip.setPixelColor(3, color)
                    strip.setBrightness(bright)
                    strip.show()
                    bright -= bright - 5
                 
                print("start lower brightness")
                sleep(1)

                strip.setPixelColor(0, color)
		strip.setPixelColor(1, color)
		strip.setPixelColor(2, color)
		strip.setPixelColor(3, color)

                strip.setBrightness(10)
		strip.show()

            sleep(0.1)
            
            if i == 4:
                sleep (0.5)                
		strip.setPixelColor(0, Color(0, 0, 0))
		strip.setPixelColor(1, Color(0, 0, 0))
		strip.setPixelColor(2, Color(0, 0, 0))
		strip.setPixelColor(3, Color(0, 0, 0))

                strip.show()

		sleep(0.1)

                strip.setPixelColor(4, color)
		strip.setPixelColor(5, color)
		strip.setPixelColor(6, color)
		strip.setPixelColor(7, color)
		strip.show()

                print("start lower brightness")
                sleep(1)

                strip.setPixelColor(4, color)
		strip.setPixelColor(5, color)
		strip.setPixelColor(6, color)
		strip.setPixelColor(7, color)
                strip.setBrightness(10)
		strip.show()
            
            if i == 8:
                sleep(0.5)
		strip.setPixelColor(4, Color(0, 0, 0))
		strip.setPixelColor(5, Color(0, 0, 0))
		strip.setPixelColor(6, Color(0, 0, 0))
		strip.setPixelColor(7, Color(0, 0, 0))

                strip.show()

		sleep(0.1)

                strip.setPixelColor(8, color)
		strip.setPixelColor(9, color)
		strip.setPixelColor(10, color)
		strip.setPixelColor(11, color)

		strip.show()

                print("start lower brightness")
                sleep(1)

                strip.setPixelColor(8, color)
		strip.setPixelColor(9, color)
		strip.setPixelColor(10, color)
		strip.setPixelColor(11, color)

                strip.setBrightness(10)
		strip.show()

                sleep(0.5)

            if i == 12:
                sleep(0.5)
		strip.setPixelColor(8, Color(0, 0, 0))
		strip.setPixelColor(9, Color(0, 0, 0))
		strip.setPixelColor(10, Color(0, 0, 0))
		strip.setPixelColor(11, Color(0, 0, 0))

                strip.show()

                sleep(0.1)		

		strip.setPixelColor(12, color)
		strip.setPixelColor(13, color)
		strip.setPixelColor(14, color)
		strip.setPixelColor(15, color)
                strip.setBrightness(15)
		strip.show()

                print("start lower brightness")
                sleep(1)
                
		strip.setPixelColor(12, color)
		strip.setPixelColor(13, color)
		strip.setPixelColor(14, color)
		strip.setPixelColor(15, color)

		strip.setBrightness(10)
                strip.show()

                sleep(0.5)

def xboxcircle(strip, color, wait_ms=25):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
                
                strip.setPixelColor((i-3)%strip.numPixels(), Color(0, 0, 0))
		strip.show()
		time.sleep(wait_ms/1000.0)

# Main program logic follows:
if __name__ == '__main__':
        # Process arguments
        opt_parse()

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
        colorWipe(strip, Color(0, 0, 0))
	print ('Press Ctrl-C to quit.')
        speed = 50
        circlecount = 5
        circlestat = 0
        colorWipe(strip, Color(0, 255, 0))
        sleep(2)
        colorWipe(strip, Color(0, 0, 0))
	while True:
                xboxcircle(strip, Color(0, 255, 0), speed) # xbox circle
                speed -= 5 if speed > 20 else 0
                if speed == 20:
                    circlestat += 1
                if circlestat == circlecount:
                    break
        colorWipe(strip, Color(0, 0, 0))
        while True:
            xboxchunk(strip, Color(0, 255, 0)) #xboxchunk

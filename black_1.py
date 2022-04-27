from re import S
import time
from rpi_ws281x import PixelStrip, Color
import sys
import json

# LED strip configuration:
LED_COUNT =     84    # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT =  False # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
# grab json from input
str_json  = json.loads(sys.argv[1].replace("'","\""))

# create image
for i in range(len(str_json)):
    strip.setPixelColor(int(i)+1,  Color(int(str_json[str(int(i)+1)].split(",")[0]),int(str_json[str(int(i)+1)].split(",")[1]),int(str_json[str(int(i)+1)].split(",")[2])))
strip.show()

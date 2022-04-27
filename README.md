# LED
Lighting an addressable led strip with a second monitor output

# What you need:

1. A raspberry pi 

2. A ws281x addressable led strip + power supply 

3. Cable to connect from the raspberry pi to the led strip

4. SSH connetivity from you PC to the raspberry

# How it works:

You have 2 files : first is the black_1.py file needs to exist on the raspberry pi and the working.py will be present on the PC.

The black_1.py file will recieve the LED colors from the PC and will transofrm them from digital to an analog signal for the LED strip.

The working.py file will create a ssh connection to the raspberry (this was faster and i don't really see a need for another service to be running on the pi) 

# How to use it:

1. copy black_1.py to your raspberry pi

2. add your raspberry ip, username and password in working.py @ line 11

3. run working.py from your PC ( will not work with Netflix content )

4. Profit



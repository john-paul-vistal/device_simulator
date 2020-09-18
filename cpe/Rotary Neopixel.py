"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 1

pos = 9
end = -1
skip = -1

while True:
    if cp.switch == False:
        for clock in range(pos,-1,-1):
            if cp.switch == True:
                pos = clock
                break
            cp.pixels[clock] = (255,255,255)
            time.sleep(0.5)
            cp.pixels[clock] = (0,0,0)
            pos = 9
    else:
        for cclock in range(pos,10,1):
            if cp.switch == False:
                pos = cclock
                break
            cp.pixels[cclock] = (255,255,255)
            time.sleep(0.5)
            cp.pixels[cclock] = (0,0,0)
            pos = 0




        



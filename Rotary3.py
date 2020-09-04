"""
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 1

pos = 9

while True:
    if cp.switch == False:
        for clock in range(pos,-1,-1):
            cp.pixels[clock] = (0,255,255)
            time.sleep(0.5)
            cp.pixels[clock] = (0,0,0)
            pos = 9
            if cp.switch == True:
                if(clock == 9):
                    pos = 0
                else:
                    pos = clock + 1 
                break
    else:
        for cclock in range(pos,10,1):
            cp.pixels[cclock] = (0,255,255)
            time.sleep(0.5)
            cp.pixels[cclock] = (0,0,0)
            pos = 0
            if cp.switch == False:
                if(cclock == 0):
                    pos = 9
                else:
                    pos = cclock - 1 
                break
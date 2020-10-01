"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import *

while True:
    light = display.read_light_level()
    peak = int(light/250*25)    
    deduct = peak * 10

    x = peak % 5
    yCheck = int(light/250*5)

    if yCheck == 0:
        y = 4
    elif yCheck == 1:
        y = 3
    elif yCheck == 2:
        y = 2
    elif yCheck == 3:
        y = 1
    elif yCheck == 4:
        y = 0

    if peak < 25:
        light = display.read_light_level()-deduct
        sleep(.1)
        display.set_pixel(x,y,light)








    

            

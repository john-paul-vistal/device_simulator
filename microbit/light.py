from microbit import *
from time import *


# y = 4
while True:
    light = display.read_light_level()
    peak = int(light/250*25)    
    deduct = peak * 10

    x = peak % 5
    # y = int(light/250*5)
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
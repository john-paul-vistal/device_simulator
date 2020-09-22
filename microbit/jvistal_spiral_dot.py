from microbit import *
import time


patern = "00000:00000:00000:00000:00000"
lpat = list(patern)

def displayLight(i):
    lpat = list(patern)
    if(lpat[i] != ':'):
        lpat[i] = "9"
    newPat = ''.join(lpat)
    img = Image(str(newPat))
    time.sleep(.5)
    display.show(img)

while True:
    for i in range(0,5):
        displayLight(i)
    for i in range(10,26,6):
        displayLight(i)
    for i in range(28,23,-1):
       displayLight(i)
    for i in range(18,4,-6):
        displayLight(i)
    for i in range(7,10):
        displayLight(i)
    for i in range(15,20,6):
        displayLight(i)
    for i in range(21,18,-1):
        displayLight(i)
    for i in range(13,7,-6):
        displayLight(i)
    for i in range(14,15,1):
        displayLight(i)
    
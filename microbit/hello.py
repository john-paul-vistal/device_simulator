from microbit import *
import time

patern = "00000:00000:00000:00000:00000"
lpat = list(patern)
while True:
    for i in range(0,len(lpat)):
        lpat = list(patern)
        if(lpat[i] != ':'):
            lpat[i] = "9"
        newPat = ''.join(lpat)
        img = Image(str(newPat))
        time.sleep(.5)
        display.show(img)

    
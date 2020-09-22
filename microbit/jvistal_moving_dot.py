from microbit import *
import time

patern = "00000:00000:00000:00000:00000"
lpat = list(patern)
while True:
    for i in range(0,len(lpat)):
        lpat = list(patern)
        if(lpat[i] != ':'):
            lpat[i] = "9"
        else:
            continue
        newPat = ''.join(lpat)
        img = Image(str(newPat))
        display.show(img)
        time.sleep(.5)

    
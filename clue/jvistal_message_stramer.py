from adafruit_clue import clue
import time

clue_data = clue.simple_text_display(title="Message Streamer", title_color=(227, 14, 14),  title_scale=2) 

rtlmsg = "This message will move from right to left... "
displaymsgrtl = "This message will move from right to left... "

ltrmsg = "This message will move from left to right ..."
displayltrmsg = "This message will move from left to right ..."
i = 0;
x = len(ltrmsg)-1
while True:

    if(i == len(rtlmsg)):
        i = 0
    if(x == 0):
        x = len(ltrmsg)-1

    clue_data[10].text = "This message blinks"  
    clue_data[10].color = clue.BLUE
    clue_data[10].scale = 2
    time.sleep(.05) 
    clue_data[10].color = clue.BLACK

    displaymsgrtl = displaymsgrtl[1:]
    displaymsgrtl += rtlmsg[i]
    clue_data[2].text = displaymsgrtl
    clue_data[2].color = clue.YELLOW
    clue_data[2].scale = 2

    displayltrmsg = displayltrmsg[:-1]
    displayltrmsg = ''.join((ltrmsg[x],displayltrmsg))
    clue_data[6].text = displayltrmsg  
    clue_data[6].color = clue.WHITE
    clue_data[6].scale = 2
   

    clue_data.show()
    i+=1
    x-=1
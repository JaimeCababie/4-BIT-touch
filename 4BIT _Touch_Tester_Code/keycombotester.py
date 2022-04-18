#4bit code
#Date 4/15/2022
#keycomobotester
import time
import board
import touchio
#key buffer and touchthreshold values
keybuff= .09
thrv = 3500
#key declaration
key1 = touchio.TouchIn(board.A0)
key2 = touchio.TouchIn(board.A1)
key3 = touchio.TouchIn(board.A2)
key4 = touchio.TouchIn(board.A3)
Change = touchio.TouchIn(board.TX)

#Key threshold value

key1.threshold = thrv
key2.threshold = thrv
key3.threshold = thrv
key4.threshold = thrv
Change.threshold = thrv

val=0


while True:
    #key value
    val=0;
    if key1.value:
        val=val+0001
    if key2.value:
        val=val+0010
    if key3.value:
        val=val+0100
    if key4.value:
        val=val+1000
    if Change.value:
        print("change")
        val=0
    if val>0:
        time.sleep(keybuff)
#comobo value
    #single keypress
    if (val==0001):
        print("0001")
    if (val==0010):
        print("0010")
    if (val==0100):
        print("0100")
    if (val==1000):
        print("1000")
    #double keypress
    if (val==0011):
        print("0011")
    if (val==1100):
        print("1100")
    if (val==0101):
        print("0101")
    if (val==1010):
        print("1010")
    if (val==0110):
        print("0110")
    if (val==1001):
        print("1001")
    #triple keypress
    if (val==0111):
        print("0111")
    if (val==1110):
        print("1110")
    if (val==1101):
        print("1101")
    if (val==1011):
        print("1011")
    #cuatriple keypress
    if (val==1111):
        print("1111")


    time.sleep(0.1)

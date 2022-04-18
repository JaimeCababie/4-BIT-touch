# Write your code here :-)
#4bit code
#Date 4/15/2022

#librerias necesarias
import time
import board
import touchio
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness=.5
#key buffer and touchthreshold values
keybuff= .1
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

val=1
profile=1
kv1=1
kv2=10
kv3=100
kv4=1000

def profilecolor(pr):
    #LED profile values
    if pr==1:
        led[0]=(255,000,000)
    if pr==2:
        led[0]=(000,255,000)
    if pr==3:
        led[0]=(000,000,255)
    if pr==4:
        led[0]=(255,000,255)



while True:
    #key value
    if Change.value:
        print("change")
        val=1
        profile=profile+1
        time.sleep(keybuff)
        if profile>4:
            profile=1
        print(profile)
    profilecolor(profile)
    val=0;
    if key1.value:
        val=profile*kv1+val
    if key2.value:
        val=profile*kv2+val
    if key3.value:
        val=profile*kv3+val
    if key4.value:
        val=profile*kv4+val
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
    print(val)

    time.sleep(0.1)



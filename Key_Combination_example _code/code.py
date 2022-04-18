#4bit Key Combinations for Windows Example Code
#Date 2022/15/05
#Version 1.00
#Jaime Cababie

#board Esentials:
import time
import board
import gc

#capacitive touch library
import touchio

#Libraies for human device interface
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keybaord_layout_us import KeyboardLayoutUS

#declare the 4BIT as an input
fourbit = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(fourbit)

#Neopixel declaration
import neopixel
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness=.5

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

#key buffer and touchthreshold values
keybuff= .09# this determines the wait time to stop double inputs
thrv = 3500# this determines the sensitivity of the keys

#key declaration
key1 = touchio.TouchIn(board.A0)
key2 = touchio.TouchIn(board.A1)
key3 = touchio.TouchIn(board.A2)
key4 = touchio.TouchIn(board.A3)
logo = touchio.TouchIn(board.TX)

#Key threshold value
key1.threshold = thrv
key2.threshold = thrv
key3.threshold = thrv
key4.threshold = thrv
logo.threshold = thrv



#Number keycode declaration:
ONE = 0X1E
TWO = 0X1F
THREE = 0X20
FOUR = 0X21
FIVE = 0X22
SIX = 0X23
SEVEN = 0X24
EIGHT = 0X25
NINE = 0X26
CERO = 0X27

#macro functions for each key combos
def action1():#0001
    #Copy
    fourbit.send(Keycode.CONTROL, Keycode.C)
def action2():#0010
    #Paste
    fourbit.send(Keycode.CONTROL, Keycode.V)
def action3():#0100
    #Cut
    fourbit.send(Keycode.CONTROL, Keycode.X)
def action4():#1000
    #Save
    fourbit.send(Keycode.CONTROL, Keycode.S)
def action5():#0011
    #undo
    fourbit.send(Keycode.CONTROL, Keycode.Z)
def action6():#1100
    #redo
    fourbit.send(Keycode.CONTROL,Keycode.Y)
def action7():#0101
    #Zoom In
    fourbit.send(Keycode.CONTROL, Keycode.EQUALS)
def action8():#1010
    #Zoom Out
    fourbit.send(Keycode.CONTROL, Keycode.MINUS)
def action9():#0110
    #screen capture
    fourbit.send(Keycode.WINDOWS, Keycode.LEFT_SHIFT,Keycode.S)
def action10():#1001
    #screen print
    fourbit.send(Keycode.PRINT_SCREEN)
def action11():#0111
    #Italics
    fourbit.send(Keycode.CONTROL, Keycode.I)
def action12():#1110
    #Bold
    fourbit.send(Keycode.CONTROL, Keycode.B)
def action13():#1101
    #Find
    fourbit.send(Keycode.CONTROL, Keycode.F)
def action14():#1011
    #Print
    fourbit.send(Keycode.CONTROL, Keycode.P)
def action15():#1111
    #select all
    fourbit.send(Keycode.CONTROL, Keycode.A)
profile=1
profilecolor(1)

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
    if logo.value:
        print("change")
        profile=profile+1
        time.sleep(keybuff)
        if profile>4:
            profile=1
    profilecolor(profile)
    if val>0:
        time.sleep(keybuff)
#comobo value
    #single keypress variations
        if (val==0001): #Action 1
            action1()
        elif (val==0010): #Action 2
            action2()
        elif (val==0100): #Action 3
            action3()
        elif (val==1000): #Action 4
            action4()
    #double keypress variations
        elif (val==0011): #Action 5
            action5()
        elif (val==1100): #Action 6
            action6()
        elif (val==0101): #Action 7
            action7()
        elif (val==1010): #Action 8
            action8()
        elif (val==0110): #Action 9
            action9()
        elif (val==1001): #Action 10
            action10()
    #triple keypress variations
        elif (val==0111): #Action 11
            action11()
        elif (val==1110): #Action 12
            action12()
        elif (val==1101): #Action 13
            action13()
        elif (val==1011): #Action 14
            action14();
    #cuatriple keypress variations
        elif (val==1111): #Action 15
            action15()
        print(val)
        gc.collect()
    time.sleep(0.1)


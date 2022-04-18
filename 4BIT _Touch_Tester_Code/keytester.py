#4bit code
#Date 4/15/2022
#Jaime Cababie

import time
import board
import touchio

#key declaration
key1 = touchio.TouchIn(board.A0)
key2 = touchio.TouchIn(board.A1)
key3 = touchio.TouchIn(board.A2)
key4 = touchio.TouchIn(board.A3)
Change = touchio.TouchIn(board.TX)
#Key threshold value
th = 4000
key1.threshold = th
key2.threshold = th
key3.threshold = th
key4.threshold = th
Change.threshold = th



while True:
    if key1.value:
        print("key1")
    if key2.value:
        print("key2")
    if key3.value:
        print("key3")
    if key4.value:
        print("key4")
    if Change.value:
        print("change")

    time.sleep(0.1)
# Write your code here :-)

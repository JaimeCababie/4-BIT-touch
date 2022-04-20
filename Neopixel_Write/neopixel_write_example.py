import board
import neopixel_write
import time
import digitalio

neo= digitalio.DigitalInOut(board.NEOPIXEL)
neo.direction = digitalio.Direction.OUTPUT
neo_power=digitalio.DigitalInOut(board.NEOPIXEL_POWER)
neo_power.direction = digitalio.Direction.OUTPUT


def set_colors(r, g, b):
    """Set both neopixels to the specified color.
    r, g, b range from 0 to 1"""
    global neo
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    pixels = bytearray([g, r, b, g, r, b])
    neopixel_write.neopixel_write(neo, pixels)

while True:
    neo_power.value= True
    set_colors(.9,.0,.0)

The neopixel_write library is a module included in CircuitPython release file for QTPY. It is a Low level method to control a single Neopixel. 

The QTPY has a Neopixel embeded in its PCB, controlled by the board.NEOPIXEL pin and the power comes from board.NEOPIXEL_POWER pin. 

It is necesary to use the neopixel_write library in the 4-BIT as including a the keyboard_layout_us library and the neopixel library created a memory error.

To use use neopixel_write module we also need to include the digitalio and board library: 

        import board 
        import neopixel_write
        import digitalio
        
Then we need to declare the pin that controls the onboard neopixel:

        neo= digitalio.DigitalInOut(board.NEOPIXEL)
        neo.direction = digitalio.Direction.OUTPUT

We also need to declare the pin that supplies power to the neopixel:

        neo_power=digitalio.DigitalInOut(board.NEOPIXEL_POWER)
        neo_power.direction = digitalio.Direction.OUTPUT

And set the NEOPIXEL_POWER pin on high to supply power to the neopixel: 

    neo_power.value= True

A set_set color function is declared to make it easer to define the color of the leds as neopixel_write module only accepts bytearrays for color values.

        def set_colors(r, g, b):
            global neo
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            pixels = bytearray([g, r, b, g, r, b])
            neopixel_write.neopixel_write(neo, pixels)

To use the function, input the RED GREEN and BLUE values in a range from 0 to 1. 

        set_colors(.6,1,0) = RED=153, GREEN=255, BLUE=0
 
 For mmore information visit the Circuit Python documentation.











Sintax for Illustrator (and other Adobe Software) commands using the 4BIT and circuitpython:

#The commands in illustrator mainly use key combinattions, because of this, it is optimal to use the fourbit.send() command. 

First we need to import the adafruit_hid libraries:

#Libraies for human device interface

	import usb_hid
	from adafruit_hid.keyboard import Keyboard
	from adafruit_hid.keycode import Keycode
	from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

	#declare the 4BIT as an input
	fourbit = Keyboard(usb_hid.devices)
	layout = KeyboardLayoutUS(fourbit) 

 Then we will use the same format as the key combination example file: 

	fourbit.send(Keycode.1KEY, Keycode.2KEY, Keycode.3KEY) #replace the "nKEY" with the letter you want to trigger.

Some command examples for Illustrator:

	#Align Text Left
	fourbit.send(Keycode.CONTROL, Keycode.RIGHT_SHIFT, Keycode.L) 

	#Align Text Right
	fourbit.send(Keycode.CONTROL, Keycode.RIGHT_SHIFT, Keycode.R) 

	#Align Text Center
	fourbit.send(Keycode.CONTROL, Keycode.RIGHT_SHIFT, Keycode.C) 

To create your own reference the Default Default Keyboard Shorcut list: 

https://helpx.adobe.com/gr_en/illustrator/using/default-keyboard-shortcuts.html



Sintax for fusion360 commands using 4BIT and circuitpython:

# To use the .write function it i necesary  to import the adafruit_hid library and to declare the layout in the code:

#Libraies for human device interface
	import usb_hid
	from adafruit_hid.keyboard import Keyboard
	from adafruit_hid.keycode import Keycode
	from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

	#declare the 4BIT as an input
	fourbit = Keyboard(usb_hid.devices)
	layout = KeyboardLayoutUS(fourbit) 

In Fusion360 you can use the letter S to search and execute tools. 

	#To execute a tool we can first press S by using:
	fourbit.send(Keycode.S)#This will toggle the search menu
	layout.write("command\n")#Then write te command you want to execute
	fourbit.send(Keycode.ENTER)#And press enter to inicilize it

Some command examples for Fusion360:
	
	fourbit.send(Keycode.S)
	layout.write("extrude\n")
	fourbit.send(Keycode.ENTER)

	fourbit.send(Keycode.S)
	layout.write("Fillet\n")
	fourbit.send(Keycode.ENTER)

	fourbit.send(Keycode.S)
	layout.write("Loft\n")
	fourbit.send(Keycode.ENTER)

	fourbit.send(Keycode.S)
	layout.write("Equal\n")
	fourbit.send(Keycode.ENTER)

	fourbit.send(Keycode.S)
	layout.write("2 point Circle\n")
	fourbit.send(Keycode.ENTER)






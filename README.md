# 4-BIT-touch
4-BIT touch is a macro pad that uses key combos to execute actions. Programed in Circuit Python. Code and PCB files available!

The 4-BIT touch uses a QTPY M0 as the mirocontroler and Circuit Python's HID library. 
There are 5 capacitive touch buttons in the PCB design four of them are ment to be used as inputs and the other one is ment to be used to change profiles. 

There are 15 key combos available when using 4 Keys as inputs: 

![Asset 1](https://user-images.githubusercontent.com/98760075/163679366-d2e5aa13-e731-4e50-bcb1-6c5d15cfeffe.png)

How does the code work: 
 
For the QTPY M0 to act as a (Human Device Interface) we need to import the adafruit_hid and usb_hid library to the code:

	import usb_hid
	from adafruit_hid.keyboard import Keyboard
	from adafruit_hid.keycode import Keycode
	from adafruit_hid.keybaord_layout_us import KeyboardLayoutUS

We also need to declare the keyboard class in the code:  

	fourbit = Keyboard(usb_hid.devices)
	layout = KeyboardLayoutUS(fourbit) # this class allows us to input strings as keyboard inputs.

To use the capacitive touch functions of the QTPY M0 we need to import the touchio library:
		
	import touchio
		
Then we need to declare the touch pins in the microcontroller.
#The capacitive touch capacitive touch pins in the QTPY are : A0, A1, A2, A3, TX, RX. 
	
The 4BIT touch has 5 touch pins enabled: A0=key1  A1=key2  A3=key3  A4=key4 and the 4BIT logo.
	
key declaration: 
	
	key1 = touchio.TouchIn(board.A0)
	key2 = touchio.TouchIn(board.A1)
	key3 = touchio.TouchIn(board.A2)
	key4 = touchio.TouchIn(board.A3)
	logo = touchio.TouchIn(board.TX)
	
The sensitivity of the keys can be change using: key.threshold = value. 
	
#In testing, the threshold value that worked the best was 3500. 
	
So a threshold variable was declared: 

	thrv= 3500 

and the threshold value was changed: 

	key1.threshold = thrv
	key2.threshold = thrv
	key3.threshold = thrv
	key4.threshold = thrv
	logo.threshold = thrv
	
The macros that the 4BIT will execute are declared inside functions called actions: 

#There are 15 diferent key combinations available, therefore there are 15 actions called in the code:

first an the function in the code is defined:
#then the macro that the 4BIT is going to execute is declared inside the function definition: 

	def action():
		#select all
 		fourbit.send(Keycode.CONTROL, Keycode.A)

Inside the While Loop the QTPY is sensing which keys are pressed:

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

When a key is pressed it adds to the value of the variaible val. 
	
To check which combination of keys are being pressed, we need to check the value of val using an if statement. 

For example:
#In this case key1, key2, key3 and key4 are being pressed.

	if (val==1111):

#In this case key1 and key4 are being pressed.

	if (val==1001):
		
When a value is equal to the If statement the action inside of the if statement is executed: 

        if (val==1111): #Action
        	action()
	#the macro inside action() is executed: fourbit.send(Keycode.CONTROL, Keycode.A)


Check out the code examples and try to make your own macros usiing the 4BIT and Circuit Python! 


The Key Codes for numbers are not included included in the keycode library for circuit python.
For this reason, it is necesary to input the keycode directly in the code like this: fourbit.send(0X1E) #this will type the number one
KeyCodes for numbers: 

  1=0X1E
  2=0X1F
  3=0X20
  4=0X21
  5=0X22
  6=0X23
  7=0X24
  8=0X25
  9=0X26
  0=0X27

You can also declare them as variables to be used later in the code: 
#Copy and paste this variables before the action definitions: 

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

Example on how to use them:

  fourbit.send(THREE)
  --this will type a 3

from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import time

GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function , pass the parameters (GPIOPins, wait(sec), steps, ccw = False/cw = True, half = half-stepping, initDelay
mymotortest.motor_run(GpioPins , .01, 100, False, False, "half", .05)

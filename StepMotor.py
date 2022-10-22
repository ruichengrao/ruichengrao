import schedule
import RPi.GPIO as GPIO

def motorSpin():

# Declare the GPIO settings
    GPIO.setmode(GPIO.BOARD)
# Connecting to GPIO Pins
    GPIO.setup(7, GPIO.OUT) # Connected to PWMA
    GPIO.setup(11, GPIO.OUT) # Connected to AIN2
    GPIO.setup(12, GPIO.OUT) # Connected to AIN1
    GPIO.setup(13, GPIO.OUT) # Connected to STBY
    print("connected to pins")

# Drive the motor clockwise
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2


# Set the motor speed
    GPIO.output(7, GPIO.HIGH) # Set PWMA (Needs to change speed)

# Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH) #For 13 sec??? 


schedule.every(5).minutes.do(motorSpin)

while True():
    schedule.run_pending()


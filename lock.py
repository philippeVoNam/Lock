# imports
import RPi.GPIO as GPIO

class Lock:
    def __init__(self):
        # set
        self.lockPin = 36

        GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
        GPIO.setup(self.lockPin, GPIO.OUT) # LED pin set as output

    # def
    def lock(self):
        GPIO.output(self.lockPin, GPIO.LOW)

    def unlock(self):
        GPIO.output(self.lockPin, GPIO.HIGH)



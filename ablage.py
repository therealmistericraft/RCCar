import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)
time.sleep(5)
GPIO.output(7, GPIO.LOW)
GPIO.cleanup()
print("Done")

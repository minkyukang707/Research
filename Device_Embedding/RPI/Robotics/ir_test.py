import PiMotor
import RPi.GPIO as GPIO
import time

ir1 = 18 # Left IR sensor
ir2 = 4 # Right IR sensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)

print("Press Control-C to end the program")

try:
    while True:
        if GPIO.input(ir1) == 0 and GPIO.input(ir2) == 0:
            print("Obstacle Detected infront of both IR sensors")
        elif GPIO.input(ir1) == 0:
            print("Obstacle Detected infront of left IR sensor")
        elif GPIO.input(ir2) == 0:
            print("Obstacle Detected infront of right IR sensor")
        print("Raw input for left and right(in order) IR sensor: ", GPIO.input(ir1), GPIO.input(ir2))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


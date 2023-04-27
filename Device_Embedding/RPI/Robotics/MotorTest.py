#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BCM) 

GPIO.setwarnings(False)

#Name of Individual MOTORS 

cal = int(config.read("motor"))
# Right Motor
if config.read("rightrev")[0] == "f":
    m2 = PiMotor.Motor("MOTOR2",1)
else:
    m2 = PiMotor.Motor("MOTOR2",2)

# Left Motor
if config.read("leftrev")[0] == "f":
    m1 = PiMotor.Motor("MOTOR1",1)
else:
    m1 = PiMotor.Motor("MOTOR1",2)

try:
    while True:
        thing_2_do = input("Enter f/b/l/r to go forward/backward/left/right, anything else to end the program: ")
        if thing_2_do == 'f':
            move_time = int(input("How long do you want to move(in seconds): "))
            m1.forward(40+cal)
            m2.forward(40)
            time.sleep(move_time)
            m1.stop()
            m2.stop()
        elif thing_2_do == 'b':
            move_time = int(input("How long do you want to move(in seconds): "))
            m1.reverse(40+cal)
            m2.reverse(40)
            time.sleep(move_time)
            m1.stop()
            m2.stop()
        elif thing_2_do == 'l':
            move_time = int(input("How long do you want to move(in seconds): "))
            m1.reverse(40+cal)
            m2.forward(40)
            time.sleep(move_time)
            m1.stop()
            m2.stop()
        elif thing_2_do == 'r':
            move_time = int(input("How long do you want to move(in seconds): "))
            m1.forward(40+cal)
            m2.reverse(40)
            time.sleep(move_time)
            m1.stop()
            m2.stop()
        else:
            break
except Exception as e:
    print('ERROR:', e)
finally:
    m1.stop()
    m2.stop()
    GPIO.cleanup()


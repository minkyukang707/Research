import PiMotor
import time
import RPi.GPIO as GPIO
from gyro import go_straight, turn_by_angle
import config

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
motor_cal = config.read("motor")

try:
    while True:
        thing_2_do = input("Enter f/b/l/r to go forward/backward/left/right, anything else will end the program: ")
        if thing_2_do == 'f':
            forward_time = input("How long(in seconds): ")
            new_sensor, thread = go_straight(50, m1, m2, motor_cal)
            time.sleep(int(forward_time))
            thread.stop()
            sensor = new_sensor
        elif thing_2_do == 'b':
            backward_time = input("How long(in seconds): ")
            new_sensor, thread = go_straight(50, m1, m2, motor_cal, direc="backward")
            time.sleep(int(backward_time))
            thread.stop()
            sensor = new_sensor
        elif thing_2_do == 'l':
            angle = input("Angle: ")
            turn_by_angle('l', int(angle), m1, m2, motor_cal)
        elif thing_2_do == 'r':
            angle = input("Angle: ")
            turn_by_angle('r', int(angle), m1, m2, motor_cal)
        else:
            break
except Exception as e:
    print('ERROR:', e)
finally:
    m1.stop()
    m2.stop()
    GPIO.cleanup()


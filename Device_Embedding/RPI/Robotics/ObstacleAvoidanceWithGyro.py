import PiMotor
import time
import RPi.GPIO as GPIO
from ultrasonic_sensor import ultra
from gyro import go_straight
import config

ir1 = 18
ir2 = 4

GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)

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

ultra = ultra()
ultra_dist = int(config.read("ultra"))
motor_cal = int(config.read("motor"))

def turn_till_clear(ir1=ir1, ir2=ir2, ultra=ultra, speed=40, m1=m1, m2=m2, cal=motor_cal, ultrad=ultra_dist):
    m1.forward(speed+cal)
    m2.reverse(speed)
    while GPIO.input(ir1) == 0 or GPIO.input(ir2) == 0 or ultra.get_dist() < ultrad:
        time.sleep(0.01)
    m1.stop()
    m2.stop()

speed = 40
ultra.start()
new_sensor, thread = go_straight(speed, m1, m2, motor_cal)

print("Press Control-C to end the program")

try:
    while True:
        if GPIO.input(ir1) == 0 or GPIO.input(ir2) == 0 or ultra.get_dist() < ultra_dist:
            thread.stop()
            turn_till_clear()
            new_sensor, thread = go_straight(speed, m1, m2, motor_cal)
except Exception as e:
    print("ERROR:", e)
except KeyboardInterrupt as ki:
    pass
finally:
    ultra.stop()
    thread.stop()
    GPIO.cleanup()


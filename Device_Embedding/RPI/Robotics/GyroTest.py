import PiMotor
import adafruit_bno055
import board
import time

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

print("This project will only use the gyro capabilities of the BNO055. Follow the documentation if you want to experiment with more of the sensor.")
print("Press Control-C to end the program.")

try:
    while True:
        print("Gyro(yaw,pitch,roll):", sensor.euler)
        time.sleep(0.1)
except KeyboardInterrupt as ki:
    pass


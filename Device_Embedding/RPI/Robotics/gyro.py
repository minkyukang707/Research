import adafruit_bno055
import threading
import board
import time

class straightThread(threading.Thread):
    def __init__(self, sensor, left_wheels, right_wheels, speed, threshold, cal, direc):
        threading.Thread.__init__(self)
        self.sensor = sensor
        self.left_wheels = left_wheels
        self.right_wheels = right_wheels
        self.speed = speed
        self.turn_stop = False
        self.threshold = threshold
        self.cal = cal
        self.direc = direc

    def get_angle(self):
        x = self.sensor.euler[0]
        if x:
            x = x % 360
            if x > 180:
                x = x-360
            return x
        return None
    
    def run(self):
        if self.direc == "forward":
            self.left_wheels.forward(self.speed+self.cal)
            self.right_wheels.forward(self.speed)
        else:
            self.left_wheels.reverse(self.speed+self.cal)
            self.right_wheels.reverse(self.speed)

        while self.turn_stop == False:
            x = self.get_angle()
            if x:
                if abs(x) > self.threshold:
                    if self.direc == "forward":
                        self.left_wheels.forward(self.speed-round(x/2.5))
                        self.right_wheels.forward(self.speed+round(x/2.5))
                    else:
                        self.left_wheels.reverse(self.speed+round(x/2.5))
                        self.right_wheels.reverse(self.speed-round(x/2.5))
            time.sleep(0.1)
    
    def stop(self):
        self.turn_stop = True
        self.join()
        self.left_wheels.stop()
        self.right_wheels.stop()

# This function starts the straightThread and to stop it going forward call straight_thread.stop()
def go_straight(speed, left_wheels, right_wheels, cal, direc="forward", threshold=5):
    i2c = board.I2C()
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    straight_thread = straightThread(sensor, left_wheels, right_wheels, speed, threshold, cal, direc)
    straight_thread.start()
    return sensor, straight_thread

def turn_by_angle(direction, angle, m1, m2, cal, speed=35):
    i2c = board.I2C()
    sensor = adafruit_bno055.BNO055_I2C(i2c)
    if direction == "r":
        m1.forward(speed+cal)
        m2.reverse(speed)
        euler = 0
        #print(euler)
        while euler < angle-5 or euler > euler+5:
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    else:
        m1.reverse(speed+cal)
        m2.forward(speed)
        euler = 0
        while euler > 365-angle or euler < 355-angle:
            time.sleep(0.01)
            euler = sensor.euler[0]
            if euler == None:
                euler = 0
    m1.stop()
    m2.stop()
    return sensor


import PiMotor
import RPi.GPIO as GPIO
import time
import threading

TRIG = 5
ECHO = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

class ultra(threading.Thread):
    def __init__(self, trig=5, echo=6):
        threading.Thread.__init__(self)
        self.trig = trig
        self.echo = echo
        self.val = None
        self.stop_thread = False
    
    def run(self):
        while self.stop_thread == False:
            GPIO.output(TRIG, False)
            time.sleep(0.1)
    
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
    
            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
    
                distance = (pulse_duration * 34300)/2
                distance = round(distance,2)
                self.val = distance
    
    def get_dist(self):
        return self.val
    
    def stop(self):
        self.stop_thread = True
        self.join()

import PiMotor
import RPi.GPIO as GPIO
import time
import threading

print("Press control c to end the program")
time.sleep(0.5)

TRIG = 5
ECHO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

try:
    while True:
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

            print("Distance to object in front of ultrasonic sensor(may not always be accurate):", distance)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


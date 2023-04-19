# https://microcontrollerslab.com/generate-delay-raspberry-pi-pico-timers-micropython/ 

#%% MicroPython Initialize Timers

from machine import Timer

timer = Timer(period=5000, mode=Timer.PERIODIC, callback=lambda t:print("Welcome to Microcontrollerslab"))

#%% Raspberry Pi Pico Timers Delay MicroPython Script

from machine import Pin, Timer        # importing pin, and timer class
led= Pin(14, Pin.OUT)                 # GPIO14 as led output

led.value(0)                          # LED is off
timer=Timer(-1)

timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))   #initializing the timer
# https://www.okdo.com/getting-started/get-started-with-raspberry-pi-pico-gpio-micropython/ 
# Micropython 사용 

#%% READ ANALOGUE INPUT
from machine import ADC, Pin
from utime import sleep
pot = ADC(26)
conversion_factor = 3.3 / 65535


while True:
    raw = pot.read_u16()
    volts = raw * conversion_factor    
    print('Raw: {} '.format(raw), 'Voltage {:.1f}V'.format(volts))
    sleep(1) 

#%% ANALOGUE INPUT & DIGITAL OUTPUT
from machine import ADC, Pin
from utime import sleep

pot = ADC(26)
led = Pin(25, Pin.OUT)

def map(s, a1, a2, b1, b2):
    return b1 + (s - a1) * (b2 - b1) / (a2 - a1)

while True:
    raw = pot.read_u16()
    delay = map(raw, 0, 65535, 0, 1)    
    print('Raw: {} '.format(raw), 'Delay {:.1f}s'.format(delay))
    led.value(1)
    sleep(delay)
    led.value(0)
    sleep(delay) 

#%% MULTI-CORE
from machine import ADC, Pin
from utime import sleep
import _thread


pot = ADC(26)
led = Pin(16, Pin.OUT)


delay = 1


def core1_task():
    global delay
    while True:
        led.value(1)
        sleep(delay)
        led.value(0)
        sleep(delay)


def map(s, a1, a2, b1, b2):
    return b1 + (s - a1) * (b2 - b1) / (a2 - a1)


_thread.start_new_thread(core1_task, ())


sleep(1) # wait for core1 to start


while True:
    raw = pot.read_u16()
    delay = map(raw, 0, 65535, 0, 1)
    print('Raw: {} '.format(raw), 'Delay {:.1f}s'.format(delay))
    sleep(0.5) 
from machine import ADC, Pin
from time import sleep

LED = Pin(16, Pin.OUT)
RotarySens = ADC(1)

while True:
    print(RotarySens.read_u16())
    if RotarySens.read_u16() < 30000:
        LED.value(1)
        sleep(0.5)

    else: 
        LED.value(0)
        sleep(0.5)    
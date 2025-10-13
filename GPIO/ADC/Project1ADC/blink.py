from machine import ADC
from time import sleep



ROTARY_SENS = ADC(0)
        
while True:
        print(ROTARY_SENS.read_u16())
        sleep(0.5)


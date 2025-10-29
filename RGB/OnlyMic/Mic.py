from ws2812 import WS2812
from machine import Pin, ADC
from utime import sleep

SoundSensor = ADC(1)

while True:
    average = 0
    for i in range (1000):
        noise = SoundSensor.read_u16()/256
        average += noise
    noise = average/1000
    print(noise)
    sleep (1)

    

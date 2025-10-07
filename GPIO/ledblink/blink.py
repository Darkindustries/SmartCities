from machine import Pin
from utime import sleep

led = Pin(16, Pin.OUT)

while True:
    led.value(1)  # Allume la LED
    sleep(1)
    led.value(0)  # Éteint la LED
    sleep(1)
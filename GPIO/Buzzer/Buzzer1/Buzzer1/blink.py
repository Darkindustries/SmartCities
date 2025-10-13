from machine import Pin, PWM, ADC,I2C
from utime import sleep

Buzzer = PWM(Pin(20))
vol = 1000

def DO():
    Buzzer.freq(1046)
    Buzzer.duty_u16(vol)

def RE():
    Buzzer.freq(1175)
    Buzzer.duty_u16(vol)

def MI():
    Buzzer.freq(1318)
    Buzzer.duty_u16(vol)

def FA():
    Buzzer.freq(1397)
    Buzzer.duty_u16(vol)

def SOL():
    Buzzer.freq(1568)
    Buzzer.duty_u16(vol)

def LA():
    Buzzer.freq(1760)
    Buzzer.duty_u16(vol)
def SI():
    Buzzer.freq(1975)
    Buzzer.duty_u16(vol)    

def NO():
    Buzzer.duty_u16(0)

while True:
    MI(); sleep(0.35)
    FA(); sleep(0.25)
    SOL(); sleep(0.6)
    MI(); sleep(0.3)
    FA(); sleep(0.25)
    SOL(); sleep(0.6)
    LA(); sleep(0.3)
    SI(); sleep(0.25)
    DO(); sleep(0.6)
    SI(); sleep(0.3)
    LA(); sleep(0.3)
    SOL(); sleep(0.6)
    FA(); sleep(0.3)
    SOL(); sleep(0.3)
    LA(); sleep(0.6)
    MI(); sleep(0.3)
    FA(); sleep(0.3)
    SOL(); sleep(0.6)
    NO(); sleep(0.2)

    # Variation (répétition douce)
    SOL(); sleep(0.4)
    LA(); sleep(0.3)
    SI(); sleep(0.5)
    DO(); sleep(0.5)
    SI(); sleep(0.3)
    LA(); sleep(0.3)
    SOL(); sleep(0.6)
    MI(); sleep(0.3)
    FA(); sleep(0.3)
    SOL(); sleep(0.6)
    NO(); sleep(0.5)

    # Final (descente douce)
    LA(); sleep(0.3)
    SOL(); sleep(0.3)
    FA(); sleep(0.4)
    MI(); sleep(0.4)
    RE(); sleep(0.4)
    DO(); sleep(0.8)
    NO(); sleep(1)
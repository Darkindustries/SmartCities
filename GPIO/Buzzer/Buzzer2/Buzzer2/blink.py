from machine import Pin, PWM, ADC, I2C
from utime import sleep

# --- Initialisation ---
Buzzer = PWM(Pin(20))
pot = ADC(2)   # potentiomètre branché sur ADC2

# volume de base (sera mis à jour à chaque lecture)
vol = 1000

# --- Lecture du potentiomètre ---
def lire_volume():
    global vol
    val = pot.read_u16()       # 0 → 65535
    vol = int(val / 65) + 300  # transforme en plage utilisable (300–1000 environ)

# --- Notes ---
def DO():
    lire_volume()
    Buzzer.freq(1046)
    Buzzer.duty_u16(vol)

def RE():
    lire_volume()
    Buzzer.freq(1175)
    Buzzer.duty_u16(vol)

def MI():
    lire_volume()
    Buzzer.freq(1318)
    Buzzer.duty_u16(vol)

def FA():
    lire_volume()
    Buzzer.freq(1397)
    Buzzer.duty_u16(vol)

def SOL():
    lire_volume()
    Buzzer.freq(1568)
    Buzzer.duty_u16(vol)

def LA():
    lire_volume()
    Buzzer.freq(1760)
    Buzzer.duty_u16(vol)

def SI():
    lire_volume()
    Buzzer.freq(1975)
    Buzzer.duty_u16(vol)

def NO():
    Buzzer.duty_u16(0)

# --- Boucle principale ---
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
    NO(); sleep(0.5)
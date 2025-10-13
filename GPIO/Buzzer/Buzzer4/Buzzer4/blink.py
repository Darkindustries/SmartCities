from machine import Pin, PWM, ADC, I2C
from utime import sleep
from lcd1602 import LCD1602
# --- Configuration des composants ---
LED = PWM(Pin(18))
Pot = ADC(2)
Button = Pin(16, Pin.IN, Pin.PULL_DOWN)
Buzzer = PWM(Pin(20))
i2C = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2C, 2, 16)

d.display()
# --- Variables globales ---
vol = 1000
musique = 0 
bp = 0          # état du bouton (0 ou 1)
last_bp = 0     # état précédent du bouton
stop_music = False  # variable pour interrompre la musique

# --- Notes en Hz ---
DO = 1046
RE = 1175
MI = 1318
FA = 1397
SOL = 1568
LA = 1760
SI = 1975
no = 0

# --- Lecture du potentiomètre ---
def lire_volume():
    global vol
    val = Pot.read_u16()        # 0 → 65535
    vol = int(val / 65)         # approx 0–1000
    return vol

# --- Détection du bouton ---
def check_bouton():
    global bp, last_bp, musique, stop_music
    bp = Button.value()
    if bp == 1 and last_bp == 0:
        musique = 1 - musique
        stop_music = True
        print("Changement de musique ! musique =", musique)
        d.clear()
        
    last_bp = bp

# --- Fonction pour jouer une note avec interruption ---
def jouer_note(freq, duree):
    global stop_music
    vol = lire_volume()
    Buzzer.freq(freq)
    Buzzer.duty_u16(vol)

    LED.freq(1000)
    lum = min(vol * 12, 65535)

    # LED allumée
    t_on = duree * 0.25
    step = 0.01
    LED.duty_u16(lum)
    t = t_on
    while t > 0:
        check_bouton()
        if stop_music:
            Buzzer.duty_u16(0)
            LED.duty_u16(0)
            return
        sleep(min(step, t))
        t -= step

    # LED éteinte
    t_off = duree * 0.75
    LED.duty_u16(0)
    t = t_off
    while t > 0:
        check_bouton()
        if stop_music:
            Buzzer.duty_u16(0)
            return
        sleep(min(step, t))
        t -= step

    Buzzer.duty_u16(0)

# --- Musiques ---
def Lord_of_the_Rings():
    d.clear()
    d.print("Lord of the Rings")
    global stop_music
    stop_music = False
    jouer_note(MI, 0.35)
    jouer_note(FA, 0.25)
    jouer_note(SOL, 0.6)
    jouer_note(MI, 0.3)
    jouer_note(FA, 0.25)
    jouer_note(SOL, 0.6)
    jouer_note(LA, 0.3)
    jouer_note(SI, 0.25)
    jouer_note(DO, 0.6)
    jouer_note(SI, 0.3)
    jouer_note(LA, 0.3)
    jouer_note(SOL, 0.6)
    jouer_note(FA, 0.3)
    jouer_note(SOL, 0.3)
    jouer_note(LA, 0.6)
    jouer_note(MI, 0.3)
    jouer_note(FA, 0.3)
    jouer_note(SOL, 0.6)
    print("Lord of the Rings ended")
    

def Super_Mario():
    d.clear()
    d.print("Super Mario")
    global stop_music
    stop_music = False
    jouer_note(MI, 0.15)
    jouer_note(MI, 0.15)
    sleep(0.15)
    jouer_note(MI, 0.15)
    sleep(0.15)
    jouer_note(DO, 0.15)
    jouer_note(MI, 0.15)
    jouer_note(SOL, 0.5)
    sleep(0.25)
    jouer_note(SOL, 0.15)
    jouer_note(LA, 0.25)
    jouer_note(FA, 0.15)
    jouer_note(SOL, 0.15)
    jouer_note(MI, 0.3)
    jouer_note(DO, 0.15)
    jouer_note(RE, 0.15)
    jouer_note(SI, 0.25)
    print("Super Mario ended")

# --- Boucle principale ---
while True:
    if musique == 0:
        Lord_of_the_Rings()
    else:
        Super_Mario()

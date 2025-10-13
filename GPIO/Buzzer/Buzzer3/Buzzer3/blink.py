from machine import Pin, PWM, ADC, I2C
from utime import sleep

LED = PWM(Pin(18))
Pot = ADC(2)
Button = Pin(16, Pin.IN, Pin.PULL_DOWN)

Buzzer = PWM(Pin(20))

Vol = 1000
musique = 0 
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
    vol = int(val / 65)   # transforme en plage utilisable (300–1000)
    return vol

# --- Fonction générique pour jouer une note et contrôler la LED ---
def jouer_note(freq, duree):
    vol = lire_volume()

    # Buzzer
    Buzzer.freq(freq)
    Buzzer.duty_u16(vol)

    # LED : intensité PWM proportionnelle au volume, flash court
    LED.freq(1000)
    lum = int(vol * 20)           # amplifie la luminosité
    if lum > 65535:
        lum = 65535

    LED.duty_u16(lum)            # LED s'allume (intensité PWM)
    sleep(duree * 0.25)          # reste allumée un court instant
    LED.duty_u16(0)              # s'éteint pour marquer le rythme
    sleep(duree * 0.75)          # reste éteinte jusqu’à la prochaine note

    # Stop le buzzer après la note
    Buzzer.duty_u16(0)

def Lord_of_the_Rings():
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
    print("musique ended")




def Super_Mario():
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
    print("musique ended")

        

while True:

    if Button.value() == 1:
        # Changement de musique quand on appuie sur le bouton
        musique = 1 - musique  # bascule entre 0 et 1
        print("Changement de musique !")
        sleep(0.3)  # anti-rebond
    if musique == 0:
        Lord_of_the_Rings()
    else:
        Super_Mario()
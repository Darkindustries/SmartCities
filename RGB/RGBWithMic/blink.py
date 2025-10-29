from machine import Pin, ADC
from ws2812 import WS2812
import utime, urandom

# --- Configuration ---
MIC_PIN = 26           # Broche ADC connectée au microphone (ex : GP26 / ADC0)
LED_PIN = 18           # Broche de la LED WS2812
NUM_LEDS = 1           # Nombre de LED RGB
SAMPLES = 200         # Nombre d’échantillons pour la moyenne
THRESHOLD = 1.1      # Seuil relatif pour détecter un pic
DEBOUNCE_MS = 100   # Délai minimal entre deux pics (ms)
FLASH_DURATION = 100   # Durée du flash LED (ms)

# --- Initialisation ---
mic = ADC(Pin(MIC_PIN))
led = WS2812(LED_PIN, NUM_LEDS)
last_beat = 0

# --- Fonctions utiles ---
def set_color(r, g, b):
    led.pixels_fill((r, g, b))
    led.pixels_show()

def random_color():
    return (urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8))

def get_average_sound(samples=100):
    total = 0
    for _ in range(samples):
        total += mic.read_u16() / 65535 * 3.3
    return total / samples

# --- Boucle principale ---
print("Demarrage du systeme de detection de pics")
set_color(0, 0, 0)

while True:
    sound_level = get_average_sound(SAMPLES)
    baseline = get_average_sound(SAMPLES)
    
    if sound_level > baseline * THRESHOLD:
        now = utime.ticks_ms()
        if utime.ticks_diff(now, last_beat) > DEBOUNCE_MS:
            # Pic détecté → LED RGB aléatoire
            color = random_color()
            set_color(*color)
            print("Pic détecte ! Couleur:", color)

            # Clignoter la LED
            utime.sleep_ms(FLASH_DURATION)
            set_color(0, 0, 0)  # éteindre la LED

            last_beat = now

    utime.sleep(0.02)

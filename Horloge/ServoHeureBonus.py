from machine import Pin, PWM, I2C
import network
import ntptime
import time
from lcd1602 import LCD1602
from ws2812 import WS2812


# ==== LedRGB ====

LED_PIN = 16           # Broche de la LED WS2812
NUM_LEDS = 1           # Nombre de LED RGB
led = WS2812(LED_PIN, NUM_LEDS)


# ==== BOUTON 12h/24h ====
button_pin = 18
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
mode_24h = False
last_button_state = button.value()


# ==== CONFIG LCD ====
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# LCD
lcd = LCD1602(i2c, 2, 16)
lcd.display()
i3c=I2C(1)


# ==== CONFIG WIFI ====
SSID = "VOTREWIFI"
PASSWORD = "MDPWIFI"

# ==== CONFIG SERVO ====
servo_pin = 20           
servo = PWM(Pin(servo_pin))
servo.freq(50)           # Fréquence du servo = 50Hz

# ==== CONFIG SERVO : conversion angle to duty cycle
def angle_to_duty(angle):
    # Servo standard : 0° = 0.5ms, 180° = 2.5ms
    # duty_u16 entre 0 et 65535
    min_duty = 1638   # 0.5ms
    max_duty = 8192   # 2.5ms
    return int(min_duty + (angle / 180) * (max_duty - min_duty))

def set_servo_angle(angle):
    servo.duty_u16(angle_to_duty(angle))
    #print(f"Servo positionne a {angle:.1f} degres ")

# ==== FONCTION HEURE D’ÉTÉ ====
def is_dst_france(t):
    # Retourne True si on est en heure d'été
    year = t[0]
    month = t[1]
    day = t[2]

    if month < 3 or month > 10:
        return False
    if month > 3 and month < 10:
        return True
    if month == 3:
        # Dernier dimanche de mars
        last_sunday = max(d for d in range(25, 32)
                          if time.localtime(time.mktime((year, 3, d, 2,0,0,0,0)))[6] == 6)
        return day >= last_sunday
    if month == 10:
        # Dernier dimanche d'octobre
        last_sunday = max(d for d in range(25, 32)
                          if time.localtime(time.mktime((year, 10, d, 3,0,0,0,0)))[6] == 6)
        return day < last_sunday
    return False

def utc_to_local(t):
    # Convertit l'heure UTC en heure locale et renvoie la saison
    offset = 1  # UTC+1 standard
    if is_dst_france(t):
        offset += 1  # UTC+2 en été
        season = "Ete"
    else:
        season = "Hiver"
    hour_local = (t[3] + offset) % 24
    return hour_local, t[4], t[5], season

# ==== CONNEXION WIFI ====
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connexion a :", SSID, end="")

    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print("Connexion a :")
    lcd.setCursor(0, 1)
    lcd.print(f"{SSID}") 

    wlan.connect(SSID, PASSWORD)
    timeout = 20  # secondes
    start = time.time()
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.5)
        if time.time() - start > timeout:
            print("\nImpossible de se connecter au Wi-Fi")
            lcd.clear()
            lcd.setCursor(0, 0)
            lcd.print("Echec de co a:")
            lcd.setCursor(0, 1)
            lcd.print(f"{SSID}") 
            break
print("\nConnecte IP :", wlan.ifconfig()[0])

# ==== SYNCHRO TEMPS NTP ====
try:
    ntptime.settime()
    print("Heure synchronisee (UTC).")
except:
    print("Erreur de synchronisation NTP")

def check_button():
    global mode_24h, last_button_state
    current_state = button.value()
    if last_button_state == 1 and current_state == 0:  # appui détecté
        mode_24h = not mode_24h
        print("Mode 24h" if mode_24h else "Mode 12h")
    last_button_state = current_state

def set_led(hour_local, minute, mode_24h):
    # Calcul luminosité : 0h = 100%, 23:59 ≈ 0%
    total_minutes = hour_local * 60 + minute
    brightness = 0.05 + 0.95 * (1 - (total_minutes / (24*60)))  # 5% min

    # Couleur selon mode
    if mode_24h:
        r, g, b = 255, 0, 0  # rouge
    else:
        r, g, b = 0, 255, 0  # vert

    # Appliquer luminosité
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)

    # Mettre à jour la LED WS2812
    led.pixels_fill((r, g, b))
    led.pixels_show()

    return brightness


# ==== BOUCLE PRINCIPALE ====
while True:
    t = time.localtime()  # UTC
    hour_local, minute, second, season = utc_to_local(t)

    check_button()


    # Calcul angle du servo selon le mode
    if mode_24h:
        angle = (hour_local + minute / 60) * (180 / 24)  # 24h sur 180° du servo
        m=2
    else:
        hour_12 = hour_local % 12
        angle = (hour_12 + minute / 60) * 15  # 12h sur 180°
        m=1

    # LED RGB
    brightness = set_led(hour_local, minute, mode_24h)

    set_servo_angle(angle)
    
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print(f"{hour_local:02d}:{minute:02d}:{second:02d} M{m}{season}")
    lcd.setCursor(0, 1)
    lcd.print(f"{angle:.1f}Deg Bri{brightness*100:3.0f}% ")

   
    time.sleep(0.01)

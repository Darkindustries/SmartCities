from machine import Pin, PWM, I2C
import network
import ntptime
import time

# ==== CONFIG WIFI ====
SSID = "VotreWIiFi"
PASSWORD = "MDPWiFi"

# ==== CONFIG SERVO ====
servo_pin = 20           # GPIO du signal du servo
servo = PWM(Pin(servo_pin))
servo.freq(50)           # Fréquence du servo = 50Hz

# Fonction pour convertir angle en duty cycle PWM
def angle_to_duty(angle):
    # Servo standard : 0° = 0.5ms, 180° = 2.5ms
    # duty_u16 entre 0 et 65535
    min_duty = 1638   # 0.5ms
    max_duty = 8192   # 2.5ms
    return int(min_duty + (angle / 180) * (max_duty - min_duty))

# Fonction pour positionner le servo
def set_servo_angle(angle):
    servo.duty_u16(angle_to_duty(angle))
    print(f"Servo positionne a {angle}degres")

# ==== CONNEXION WIFI ====
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connexion a : ",SSID, end="")
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(0.5)
print("\nConnecte IP :", wlan.ifconfig()[0])

# ==== SYNCHRO TEMPS ====
try:
    ntptime.settime()
    print("Heure synchronisee (UTC).")
except:
    print("Erreur de synchronisation NTP")

# ==== BOUCLE PRINCIPALE ====
while True:
    t = time.localtime()
    hour = t[3] % 12
    minute = t[4]

    # 0h = 0°, 6h = 90°, 12h = 180°
    angle = (hour + minute / 60) * 15
   
    set_servo_angle(angle)
    print(f"Heure : {hour:02d}:{minute:02d}")

    time.sleep(10)

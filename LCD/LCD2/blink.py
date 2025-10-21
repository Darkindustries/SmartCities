from machine import Pin, PWM, ADC, I2C
from time import ticks_ms, ticks_diff, sleep
from lcd1602 import LCD1602
from dht20 import DHT20

# Initialisation des broches
buzzer = PWM(Pin(18))                  
ROTARY_ANGLE_SENSOR = ADC(2)  

# Initialisation de la LED
LED = Pin(20, Pin.OUT)                 
LED.value(0)
last_led_toggle = 0
led_state = False



# I2C pour LCD et DHT20 sur même bus
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# LCD
lcd = LCD1602(i2c, 2, 16)
lcd.display()
i3c=I2C(1)
last_alarm_blink = 0
alarm_visible = False

# Capteur DHT20
dht20 = DHT20(i3c)
last_hum_read = 0        # Dernier instant de lecture
hum = 0.0  
last_temp_read = 0        # Dernier instant de lecture
temp = 0.0  

# --- Fonction : lire l’humidité toutes les 1 seconde ---
def read_humidity_every_second():
    global last_hum_read, hum
    current_time = ticks_ms()

    if ticks_diff(current_time, last_hum_read) >= 1000:
        hum = dht20.dht20_humidity()
        last_hum_read = current_time

    return hum


# --- Fonction : lire la température toutes les 1 seconde ---
def read_temp_every_second():
    global last_temp_read, temp
    current_time = ticks_ms()

    if ticks_diff(current_time, last_temp_read) >= 1000:
        temp = dht20.dht20_temperature()
        last_temp_read = current_time

    return temp


# --- Contrôle LED et Buzzer ---
def control_outputs(temp, consigne):
    global led_state, last_led_toggle

    now = ticks_ms()
    diff = temp - consigne

    # Pas d'alarme : tout est éteint
    if diff <= 0:
        LED.value(0)
        buzzer.duty_u16(0)
        return "OK"

    # Si température > consigne
    elif 0 < diff <= 3:
        # LED bat à 0,5 Hz (toutes les 1s)
        if ticks_diff(now, last_led_toggle) >= 1000:
            led_state = not led_state
            LED.value(led_state)
            last_led_toggle = now
        buzzer.duty_u16(0)
        return "WARN"

    # Si température > consigne + 3°C
    else:
        # LED clignote vite (5 Hz -> toutes les 100 ms)
        if ticks_diff(now, last_led_toggle) >= 100:
            led_state = not led_state
            LED.value(led_state)
            last_led_toggle = now
        buzzer.freq(1000)
        buzzer.duty_u16(30000)  # buzzer ON
        return "ALARM"
    



    # --- Clignotement du mot ALARM ---
def display_alarm_blink():
    """Fait clignoter le mot 'ALARM' sur l’écran LCD."""
    global last_alarm_blink, alarm_visible
    now = ticks_ms()

    if ticks_diff(now, last_alarm_blink) >= 500:  # change toutes les 0.5s
        alarm_visible = not alarm_visible
        last_alarm_blink = now

    if alarm_visible:
        lcd.setCursor(10, 1)
        lcd.print("ALARM")
    else:
        lcd.setCursor(10, 1)
        lcd.print("     ")  # efface le mot





# --- Boucle principale ---
while True:
    temp_value = read_temp_every_second()
    
    ADC_value = ROTARY_ANGLE_SENSOR.read_u16()

    # Conversion linéaire (160–65535 → 15–35)
    mapped_value = 15 + (ADC_value - 160) * (35 - 15) / (65535 - 160)

    state = control_outputs(temp_value, mapped_value)


    
    lcd.setCursor(0, 0)
    lcd.print("Ambient:" + str(round(temp_value, 1)))
    lcd.setCursor(0, 1)
    lcd.print("set:" + str(round(mapped_value, 1)))

   # Clignotement du mot ALARM
    if state == "ALARM":
        display_alarm_blink()
    else:
        # Si pas en alarme → effacer la zone
        lcd.setCursor(10, 1)
        lcd.print("     ")

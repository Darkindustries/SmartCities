import machine
import utime

button = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(16, machine.Pin.OUT)

val = 0
last_button = 0
last_toggle = utime.ticks_ms()
led_state = 0

while True:
    # Détection front montant (sans anti-rebond)
    current_button = button.value()
    if current_button == 1 and last_button == 0:
        val = (val + 1) % 3
    last_button = current_button

    now = utime.ticks_ms()

    if val == 0:
        # Clignote à 0,5 Hz (1s ON, 1s OFF)
        interval = 1000
    elif val == 1:
        # Clignote rapide (4 Hz)
        interval = 125
    elif val == 2:
        led.value(0)
        continue

    if utime.ticks_diff(now, last_toggle) > interval:
        led_state = not led_state
        led.value(led_state)
        last_toggle = now


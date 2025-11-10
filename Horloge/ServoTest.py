from machine import Pin, PWM
import time

# ==== CONFIG SERVO ====
servo_pin = 20           # GPIO du signal du servo
servo = PWM(Pin(servo_pin))
servo.freq(50)           # Fréquence standard des servos = 50Hz

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
    print(f"Servo positionné à {angle}°")

# ==== TEST DU SERVO ====
angles = [0, 90, 180]  # angles de test


while True:
    for a in angles:
        set_servo_angle(a)
        time.sleep(1)  # délai pour que le servo bouge

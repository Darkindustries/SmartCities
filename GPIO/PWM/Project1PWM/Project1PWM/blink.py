from machine import Pin, PWM
import utime

LED_PWM = PWM(Pin(18))

val=0
LED_PWM.freq(500)
while True:
    while val<65500:
        val=val+50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)
    
    while val>0:
        val=val-50
        utime.sleep_ms(1)
        LED_PWM.duty_u16(val)


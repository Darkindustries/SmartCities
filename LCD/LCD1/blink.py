from machine import Pin, PWM, ADC, I2C
from time import sleep
from lcd1602 import LCD1602
from dht20 import DHT20

# Initialisation des broches
buzzer = PWM(Pin(18))                  
ROTARY_ANGLE_SENSOR = ADC(2)           
LED = Pin(20, Pin.OUT)                 
LED.value(0)

# I2C pour LCD et DHT20 sur même bus
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# LCD
lcd = LCD1602(i2c, 2, 16)
lcd.display()
i3c=I2C(1)
# Capteur DHT20
dht20 = DHT20(i3c)





note_index = 0
while True:
   
    temp = dht20.dht20_temperature()
    hum = dht20.dht20_humidity()
    ADC_value = ROTARY_ANGLE_SENSOR.read_u16()
    lcd.clear()
    lcd.setCursor(0,0)
    lcd.print("Temp: " + str(temp) )
    lcd.setCursor(0,1)

    lcd.print("adc:" + str(ADC_value) )

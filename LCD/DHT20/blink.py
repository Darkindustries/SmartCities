from machine import Pin, I2C
from utime import sleep
from dht20 import DHT20

dhti2C = I2C(1)
dht20 = DHT20(dhti2C)

while True:
    temper = dht20.dht20_temperature()
    humi = dht20.dht20_humidity()
    print("Temperature: " + str(temper) + " C")
    print("Humidity: " + str(humi) + "%")
    sleep(1)

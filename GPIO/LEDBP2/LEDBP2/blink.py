import time
import machine
import random  # pour générer les nombres aléatoires
led = machine.Pin(18, machine.Pin.OUT)
Button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
NbrAppui = 0

 
def changerMode(pin):
    global NbrAppui
    if(Button.value() == 1):
        NbrAppui += 1
        if(NbrAppui == 7):
            NbrAppui = 0
 
Button.irq(trigger=machine.Pin.IRQ_RISING, handler=changerMode)
 
while(True):  
 
    if(NbrAppui == 1):
       
        led.value(1)
        time.sleep(0.5)
        led.value(0)
        time.sleep(0.5)
   
    if(NbrAppui == 2):
       
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    if(NbrAppui == 3):
        
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)
   
    if(NbrAppui == 4):
        
        led.value(1)
        time.sleep(0.01)
        led.value(0)
        time.sleep(0.01)
    if NbrAppui == 5:
        # Clignotement avec délais aléatoires entre 0.05s et 0.2s
        on_time = random.uniform(0.05, 0.2)
        off_time = random.uniform(0.05, 0.2)
        led.value(1)
        time.sleep(on_time)
        led.value(0)
        time.sleep(off_time)

    if(NbrAppui == 6):
        led.value(0)
 
    time.sleep(0.1)
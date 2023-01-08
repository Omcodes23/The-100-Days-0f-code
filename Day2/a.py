from machine import Pin
import time
import urequests

def start():
    a = Pin(0 , Pin.IN , Pin.PULL_UP) # D3
    d = Pin(4 , Pin.IN  , Pin.PULL_UP) # D2
    w = Pin(5 , Pin.IN , Pin.PULL_UP) # D1
    s = Pin(12 , Pin.IN , Pin.PULL_UP) # D6
    
    
    while True :
        if a.value() == 0:
            urequests.get(url = 'http://192.168.137.1:8999/a')
            print("sent a")
        elif d.value() == 0:
            urequests.get(url = 'http://192.168.137.1:8999/d')
            print("sent d")
        elif w.value() == 0:
            urequests.get(url = 'http://192.168.137.1:8999/w')
            print("sent w")
        elif s.value() == 0:
            urequests.get(url = 'http://192.168.137.1:8999/s')
            print("sent s")
        else :
            time.sleep_ms(100)


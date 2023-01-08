from machine import Pin
import time
def p(p):
    p = int(p)
    Pin(p,Pin.OUT).value(not Pin(p,Pin.OUT).value())

def blink(p , t):
    p = int(p)
    t = int(t)
    print("press ctrl + c to stop")
    while True:
        try :
            Pin(p,Pin.OUT).off()
            time.sleep_ms(t)
            Pin(p,Pin.OUT).on()
            time.sleep_ms(t)
        except KeyboardInterrupt :
            print("stopped blinking")
            break
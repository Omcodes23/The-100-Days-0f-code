import network
import led
import time


sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("vivo 1820", "12345678")

while True :
    if sta_if.isconnected() == True :
        led.p(14)
        led.p(14)
        break
    else :
        pass

time.sleep(5)
led.p(14)

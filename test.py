import time
from neopixel import *
from gledmatrix import *


# myled = GLED(count=1260,pin=18,len=21,height=60)
myled = GLED(count=5400,pin=21,len=90,height=60)

while True :
    myled.setBrightness(1)
    myled.setAllColor(Color(0,0,255))
    time.sleep(2)
    myled.setBrightness(1)
    myled.setAllColor(Color(0,255,0))
    time.sleep(2)
    myled.setBrightness(1)
    myled.setAllColor(Color(255,0,0))
    time.sleep(2)

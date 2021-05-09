import librosa
import numpy as np
from gledmatrix import *
from gaudio import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
args = parser.parse_args()
print ('Press Ctrl-C to quit.')
if not args.clear:
    print('Use "-c" argument to clear LEDs on exit')

myled = GLED(count=5400,pin=21,len=90,height=60) 
wait_ms = 50

path = './爱-小虎队.mp3'
myaudio = GAUDIO(path)

def case1():
    coords = myaudio.rolloff2coords(myled.getMatrixSize()[0],myled.getMatrixSize()[1])  
    for i in range(len(coords)):
        myaudio.showListColor(coords[i])
        time.sleep(wait_ms/1000)
        myled.clearMatrix()
def case2():
    myled.showRainbowCycle(wait_ms=rms)
def case3():
    myled.showCrossFlash(Color(123,123,235),wait_ms=myaudio.beats2sth)
def case4():
    
switch = {'case1': case1,               
          'case2': case2,
          'case3': case3,
          'case4': case4,
          }
try:
    switch.get('case1', default)()  # 执行对应的函数，如果没有就执行默认的函数


except KeyboardInterrupt:
    if args.clear:
        myled.clearMatrix()


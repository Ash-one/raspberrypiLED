import librosa
import numpy as np
from Matrix.MatrixController import *
# from gaudio import *
import pickle

with open('../Output/result.pk', 'rb') as f:
    finallist = pickle.load(f)

print(finallist)
myled = GLED(count=5400,pin=21,len=90,height=60)
wait_ms = 50



for dict in finallist:
    myled.setBrightness(dict['brightness'])
    myled.showPixelList(dict['coord'])
    time.sleep(wait_ms/1000)


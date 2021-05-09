import librosa
from sklearn.preprocessing import MinMaxScaler,scale
import numpy as np
import matplotlib.pyplot as plt
from Animation.Fence.FenceAnimation import FenceAnimation
from Animation.Dot.DotAnimation import DotAnimation
from Animation.Dot.ShakeDotAnimation import ShakeDotAnimation
from Animation.Dot.SpiralDotAnimation import SpiralDotAnimation
from Animation.Circle.CircleAnimation import CircleAnimation
from Animation.Polygon.PolygonAnimation import PolygonAnimation
from Animation.Explosion.ExplosionAnimation import ExplosionAnimation

class Pixel(object):
    def __init__(self,coord:list,rgb:list):
        self.coord = coord
        self.rgb = rgb


def emotion2H(emotion:int):
    if emotion==1:
        return np.random.randint(200,290)
    elif emotion==2:
        return np.random.randint(90,200)
    elif emotion==3:
        return np.random.randint(0,40)
    elif emotion==4:
        return np.random.randint(40,90)
    elif emotion==5:
        return np.random.randint(300,400)%360

def HSI2RGB(H,S,I):
    '''
    H 为色调，度数0-355
    S 为饱和度，0-100
    I 为亮度，0-100
    返回RGB，范围0-255
    '''
    S = S/100
    I = I/100
    R=G=B=0
    if H == 0:
        R = I + 2*I*S
        G = I - I*S
        B = I - I*S
    elif 0 < H < 120:
        H = np.pi/180 * H
        R = I + I*S*np.cos(H)/np.cos(np.pi/3-H)
        B = I - I*S
        G = 3*I - (G+B)
    elif H == 120:
        R = I - I*S
        G = I + 2*I*S
        B = I - I*S
    elif 120 < H < 240:
        H = np.pi/180 * H
        R = I - I*S
        G = I + I*S*np.cos(H-2*np.pi/3)/np.cos(np.pi-H)
        B = I + I*S*(1-np.cos(H-2*np.pi/3)/np.cos(np.pi-H))
    elif H == 240:
        R = I - I*S
        G = I - I*S
        B = I + 2*I*S
    elif 240 < H < 360:
        H = np.pi/180 * H
        R = I + I*S*(1-np.cos(H-4*np.pi/3)/np.cos(5*np.pi/3-H))
        G = I - I*S
        B = I + I*S*np.cos(H-4*np.pi/3)/np.cos(5*np.pi/3-H)
    if G > 1:
        G = 1
    if R > 1:
        R = 1
    if B > 1:
        B = 1
    R,G,B = round(R*255),round(G*255),round(B*255)

    return [R,G,B]

def myMinMaxScale(multiple,list):
    return multiple/(max(list)-min(list))*(list-min(list))

y,sr = librosa.load('爱不爱我-零点乐队.wav')
Y = librosa.stft(y, n_fft=4096, hop_length=2205, win_length=2205)
S, phase = librosa.magphase(Y)

# rmse = librosa.feature.rms(y=y, hop_length=2205)[0]
# # print(rmse.shape,rmse)
# rmse = rmse*100.0/max(abs(rmse))
# # print(rmse.shape,rmse)

zcr = librosa.feature.zero_crossing_rate(y=y,hop_length=2205)[0]
zcr = np.round(zcr*100)


def zcrAnimation(zcr_frame,sustain,color):
    ani = ExplosionAnimation(sustain=sustain,count=zcr_frame)
    l = ani.createAnimation()
    pixels = []
    for i in l:
        framePixels=[]
        for j in i:
            framePixels.append(Pixel(coord=j,rgb=color))
        pixels.append(framePixels)
    return pixels



def flatnessAnimation(flatness_frame,sustain,color):
    ani = SpiralDotAnimation(sustain=sustain,count=flatness_frame)
    l = ani.createAnimation()
    pixels = []
    for i in l:
        framePixels=[]
        for j in i:
            framePixels.append(Pixel(coord=j,rgb=color))
        pixels.append(framePixels)
    return pixels

def rolloffAnimation(rolloff_frame,sustain,color):
    ani = ShakeDotAnimation(sustain=sustain,count=rolloff_frame)
    l = ani.createAnimation()
    pixels = []
    for i in l:
        framePixels=[]
        for j in i:
            framePixels.append(Pixel(coord=j,rgb=color))
        pixels.append(framePixels)
    return pixels

def contrastAnimation(contrast_frame,sustain,color):
    ani = FenceAnimation(sustain=sustain,count=contrast_frame,square=False )
    l = ani.createAnimation()
    pixels = []
    for i in l:
        framePixels=[]
        for j in i:
            framePixels.append(Pixel(coord=j,rgb=color))
        pixels.append(framePixels)
    return pixels

# contrast = librosa.feature.spectral_contrast(S=np.abs(Y), sr=sr).T
# spec_contrast = []
# for con in contrast:
#     spec_contrast.append(np.mean(con))
# spec_contrast = np.round(myMinMaxScale(4,spec_contrast)+4)
#
# print(spec_contrast.__len__(),spec_contrast)
#
# plt.plot(spec_contrast)
# plt.show()
#
# print(zcr.shape,zcr)
# onset_env = librosa.onset.onset_strength(sr=sr, S=np.abs(Y), aggregate=np.median)
# tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
# print(beats.shape,beats)
#
# Ydb = librosa.amplitude_to_db(np.abs(Y))  # 把幅度转成分贝格式
# Ydb = Ydb.mean(axis=0)
# # print(Ydb.shape,Ydb)
# Ydb = 100/(max(Ydb)-min(Ydb))*(Ydb-min(Ydb))
# print(Ydb.shape,Ydb)

# H = np.random.randint(0,360)%360
# H = 0
# S = rmse[1]
# I = Ydb[1]
# R,G,B = HSI2RGB(H,S,I)
# print('hsi:',H,S,I)
# print('rgb:',R, G, B)

#
# spec_flatness = librosa.feature.spectral_flatness(S=S)[0]
# print(spec_flatness.shape,spec_flatness)
# spec_flatness = myMinMaxScale(200,spec_flatness)
# print(spec_flatness.shape,spec_flatness)
#
# rolloff = librosa.feature.spectral_rolloff(y=y, hop_length=2205)[0]
# rolloff = np.log2(rolloff)
# rolloff = myMinMaxScale(100,rolloff)
# print(rolloff.shape,rolloff)

# plt.plot(beats)
# plt.show()


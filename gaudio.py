import librosa
import numpy as np
from gledmatrix import *

class GAUDIO(Object):
    def __init__(self,path):
        audio_path = path
        y, sr = librosa.load(audio_path, sr=None)

        Y = librosa.stft(y,n_fft=4096,hop_length=2205,win_length=2205) # frames:5387,beats:134 以50ms为一帧 size:（2049，5387）
        # Y = librosa.stft(y)                                          # 默认hop_length = 512,win_length = 2048  frames:23197,beats:535

        S,phase = librosa.magphase(Y)
        absY = np.abs(Y)
        
        rms = librosa.feature.rms(S)[0]                                # rms 转换为彩虹流动
        rolloff = librosa.feature.spectral_rolloff(S=S, sr=sr)[0]      # rolloff转换为三角函数图像

    # beats + tempo，返回wait_ms
    def beats2sth(self):
        onset_env = librosa.onset.onset_strength(sr=sr,S=absY,aggregate = np.median)
        tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
        print('len_beats:',len(beats))
        print('beats',beats)
        wait_ms = np.around(60/tempo)

        return wait_ms


    #  将响度db转换为亮度，返回一个亮度list
    def db2br(self,absY):
        Ydb = librosa.amplitude_to_db(absY)   # 把幅度转成分贝格式
        Adb = np.zeros_like(Ydb[0])
        brightness = np.zeros_like(Adb,dtype=int)

        for j in range(Ydb.shape[1]):
            for i in range(Ydb.shape[0]):
                Adb[j]+=Ydb[i][j]

        Adb = np.divide(Adb,Ydb.shape[0])
        Adb = np.add(Adb,100)       # 使其全部为正，参数暂定
        Adb = np.log2(Adb)
        max = np.max(Adb)
        min = np.min(Adb)

        # 映射到亮度0-255的区间上
        for i in range(len(Adb)):
            Adb[i] = 255/(max-min)*(Adb[i]-min)
            brightness[i] = np.around(Adb[i])

        return brightness

    
    # rolloff转换为三角函数图像，返回一个坐标list
    def rolloff2sth(self,r,length,height):
        graphx = np.linspace(0,length-1,length,endpoint=True)
        A = np.log2(r)
        if (A > height/2):      # A是振幅，应小于矩阵的高的一半
            A = np.log2(A)
        phi = height/2          # 偏移去掉负值，phi取矩阵的高的一半
        graphy = A * np.sin(0.3 * graphx) + phi
        graphy = np.round(graphy)
        coord = []
        for i in range(len(graphx)):
            coord.append((int(graphx[i]), int(graphy[i])))
        return coord

    def rolloff2coords(self,length,height):
        coords = []
        for i in range(len(rolloff)):
            coord = rolloff2sth(rolloff[i],length,height)
            coords.append(coord)
        return coords


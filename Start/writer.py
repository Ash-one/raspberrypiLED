import librosa
import numpy as np
from sklearn import svm
from Audio.tools import emotion2H,HSI2RGB,myMinMaxScale,zcrAnimation,contrastAnimation,flatnessAnimation,rolloffAnimation
import joblib
import pickle

music_path = '怒放的生命-汪峰.wav'

y,sr = librosa.load(music_path, sr=44100)
Y = librosa.stft(y, n_fft=4096, hop_length=2205, win_length=2205)
S, phase = librosa.magphase(Y)

sustain = 40

# 等比放缩对应饱和度S
rmse = librosa.feature.rms(y=y, hop_length=2205)[0]
hsi_S = rmse*100.0/max(abs(rmse))
frames_num = len(rmse)
print(frames_num)

# 线性放缩对应亮度I
Ydb = librosa.amplitude_to_db(np.abs(Y))  # 把幅度转成分贝格式
Ydb = Ydb.mean(axis=0)
hsi_I = 100/(max(Ydb)-min(Ydb))*(Ydb-min(Ydb))

# 按帧对应亮度提升
onset_env = librosa.onset.onset_strength(sr=sr, S=np.abs(Y), aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

# 线性放缩对应螺旋线
spec_flatness = librosa.feature.spectral_flatness(S=S)[0]
spec_flatness = myMinMaxScale(200,spec_flatness)

# 非线性变换对应随机点和晃动点
rolloff = librosa.feature.spectral_rolloff(y=y, hop_length=2205)[0]
rolloff = np.log2(rolloff)
rolloff = myMinMaxScale(100,rolloff)

# 线性映射对应爆炸
zcr = librosa.feature.zero_crossing_rate(y=y,hop_length=2205)[0]
zcr = np.round(zcr*100)

# 等比缩放对应栅栏
contrast = librosa.feature.spectral_contrast(S=np.abs(Y), sr=sr).T
spec_contrast = []
for con in contrast:
    spec_contrast.append(np.mean(con))
spec_contrast = np.round(myMinMaxScale(4,spec_contrast)+4)

model = joblib.load('../Audio/emotion.model')


finallist = []
for i in range(0,frames_num-1,sustain):

    explosion = zcrAnimation(zcr[i],sustain=sustain,color=HSI2RGB(emotion2H(1),hsi_S[i],hsi_I[i]))
    fence = contrastAnimation(spec_contrast[i],sustain=sustain,color=HSI2RGB(emotion2H(1),hsi_S[i],hsi_I[i]))
    spiral = flatnessAnimation(spec_flatness[i],sustain=sustain,color=HSI2RGB(emotion2H(1),hsi_S[i],hsi_I[i]))
    shake = rolloffAnimation(rolloff[i],sustain=sustain,color=HSI2RGB(emotion2H(1),hsi_S[i],hsi_I[i]))

    for j in range(sustain):
        dict = {}
        if i+j < frames_num:
            dict['brightness']=np.round(hsi_I[i+j])
        else:
            dict['brightness']=np.round(hsi_I[frames_num-1])
        dict['coords'] = explosion[j]+fence[j]+spiral[j]+shake[j]
        finallist.append(dict)

with open('../Output/result.pk', 'wb') as f:
    pickle.dump(finallist, f)


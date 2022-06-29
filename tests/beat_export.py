import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
from itertools import cycle

filename = './sounds/restmycase.mp3'

y, sr = librosa.load(filename)
# fig, ax = plt.subplots(nrows=3, sharex=True)

y_harm, y_perc = librosa.effects.hpss(y)

onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                         aggregate=np.median)
tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,
                                       sr=sr)
print("tempo is", tempo)
beattime = librosa.frames_to_time(beats, sr=sr)
print("beats is", beattime)

print("starting exporting")

def addSection(inf, filename, tracktime):
    inf.append("file %s"%(filename))
    inf.append("outpoint %s"%(tracktime))

inf = []
images = ["01.png", "02.png"]
pool = cycle(images)

prev = beattime[0]
addSection(inf, next(pool), prev)

for x in beattime[1:]:
    diff = x - prev
    addSection(inf, next(pool), diff)
    prev = x

with open('sounds/in.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(inf))

print("Write in.txt successfully!")
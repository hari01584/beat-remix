import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

filename = './sounds/playdate.mp3'

y, sr = librosa.load(filename)
# fig, ax = plt.subplots(nrows=3, sharex=True)

y_harm, y_perc = librosa.effects.hpss(y)

tempo, beats = librosa.beat.beat_track(y=y_perc, sr=sr)
print("tempo is", tempo)
beattime = librosa.frames_to_time(beats, sr=sr)
print("beats is", beattime)

for s in range(0,len(y_perc),sr):
    print(y[s:s+sr])
    break

# y_perc = np.abs(librosa.stft(y_perc, hop_length=512))
# y_perc = librosa.amplitude_to_db(y_perc, ref=np.max)

# librosa.display.waveshow(y_harm, sr=sr, alpha=0.5, ax=ax[2], label='Harmonic')
# librosa.display.waveshow(y_perc, sr=sr, color='r', alpha=0.5, ax=ax[2], label='Percussive')
# ax[2].set(title='Multiple waveforms')
# ax[2].legend()

# plt.show()
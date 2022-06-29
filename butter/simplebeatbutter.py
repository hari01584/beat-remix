# --- SimpleBeatButter : Process sound using butter/knife functions --- #

import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
from itertools import cycle

class SimpleBeatButter:
    def __init__(self, music):
        self.music = music

    def butter(self):
        print("Starting butter")
        y, sr = librosa.load(self.music)
        y_harm, y_perc = librosa.effects.hpss(y)
        tempo, beats = librosa.beat.beat_track(y=y_perc, sr=sr)
        print("tempo is", tempo)
        beattime = librosa.frames_to_time(beats, sr=sr)
        self._knife = beattime


    def knife(self):
        return self._knife
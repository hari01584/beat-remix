
# --- SimpleHoneyMerger : Merge sound timestamps with image using simple honey/toast functions --- #

import numpy as np
from itertools import cycle
import os
import subprocess
import shlex

def _addSection(inf, filename, tracktime):
    inf.append("file %s"%(filename))
    inf.append("outpoint %s"%(tracktime))

class SimpleHoneyMerger:
    def __init__(self, timestamp, images, sound):
        self.timestamp = timestamp
        self.images = cycle(images)
        self._toast = []
        self.sound = sound

    def honey(self):
        print("Starting simple honey merger")
        prev = self.timestamp[0]
        _addSection(self._toast, next(self.images), prev)
        for x in self.timestamp[1:]:
            diff = x - prev
            _addSection(self._toast, next(self.images), diff)
            prev = x
    
    def __ffmpeg(self):
        if not os.path.exists("output/"):
            os.makedirs("output/")

        command = "ffmpeg -i %s -f concat -i %s -c:v libx264 -pix_fmt yuv420p -vf scale=320:240 -acodec copy -shortest %s" % (self.sound, "in.txt", "output/"+os.path.splitext(os.path.basename(self.sound))[0]+".mp4")
        print(command)

        print("Starting builder final")
        cmd = shlex.split(command)
        subprocess.call(cmd)
        print("Successfully built! Output files in output directory! Check console for any errors.")


    def toast(self):
        with open('in.txt', mode='wt', encoding='utf-8') as myfile:
            myfile.write('\n'.join(self._toast))

        print("Write in.txt successfully!")

        print("building from ffmpeg")
        self.__ffmpeg()
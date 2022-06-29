from scripts.chooser import get_choice, choose
import os, random

SUFFIX_SOUND = ("wav", "mp3")

def _datasetSound(root, file):
    return os.path.join(root, file)

def datasetSound():
    root = "sounds"
    files= [file for file in os.listdir(root) if file.endswith(SUFFIX_SOUND)]
    print("Choose an audio")
    fn = choose(files)
    soundfile = files[fn]
    return _datasetSound(root, soundfile)
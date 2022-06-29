from scripts.chooser import get_choice, choose
import os, random

def _datasetImages(n, root, folder, sampling):
    subf = os.path.join(root, folder)
    f = os.listdir(subf)
    files = []
    for ff in f:
        files.append(os.path.join(subf, ff))

    if(sampling == 0):
        files = random.sample(files, min(len(files), n))
        return files
    else:
        return files[:min(len(files), n)]

def datasetImages(n):
    root = "images"
    folders = os.listdir(root)
    print("Choose images folder: ")
    folder = choose(folders)
    fname = folders[folder]
    print("You selected %s"%fname)

    print("Choose sampling method")
    x = choose(["Random","Alphabetical"])

    return _datasetImages(n, root, fname, x)
from image_selector import datasetImages, _datasetImages
from sound_selector import datasetSound, _datasetSound

# --- Get Sound --- #
# sound = _datasetSound("sounds", "restmycase.mp3")
sound = datasetSound()

# --- Using simple beat butter --- #
from butter.simplebeatbutter import SimpleBeatButter
butter = SimpleBeatButter(sound)
butter.butter() # Starts processing data
timestamps = butter.knife() # Return results

# --- Get images --- #
# images = _datasetImages(len(timestamps), "images", "animepos", 0)
images = datasetImages(len(timestamps))

# --- Merge timestamp --- #
from honey.simple_honey_merger import SimpleHoneyMerger
honey = SimpleHoneyMerger(timestamps, images, sound)
honey.honey()
honey.toast()
from image_selector import datasetImages, _datasetImages
from sound_selector import datasetSound, _datasetSound
from scripts.chooser import get_choice, choose

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

# --- Ask info ---- #
video_specs = {
    "1080x1920 (Landscape) - (Instagram, Reels, Portrait)":"1080:1920",
    "1920x1080 (Wide, 16:9) - (Youtube)": "1920:1080",
    "1080x720 (Normal, 4:3)": "1080:720",
}
lst = [*video_specs]
choice = choose(lst)
dimen = video_specs[lst[choice]]
print("You chose:", lst[choice], "thf. dimen passed:", dimen)
# --- Merge timestamp --- #
from honey.simple_honey_merger import SimpleHoneyMerger
honey = SimpleHoneyMerger(timestamps, images, sound, dimen)
honey.honey()
honey.toast()
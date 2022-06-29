
# BeatRemix

Mix sound with images to create montage/edits using the rhymthic beats!

BeatRemix identifies the beats in a sound file and using it generate an edit video containing images that change according to the flow/beats! All the work is proof-of-concept and is subpar at best but it demonstrates the capability to automatically generate cool edits without using any video editors/etc!
## Demo

![output](https://user-images.githubusercontent.com/31770598/176458820-c085bb82-e601-43eb-9d3d-b33b6c64e155.gif)

Youtube video link with ASMR typing sounds [here](https://youtu.be/wUvmkqL6j4k)

__Sample Output Video (Do watch it): [(Katy Perry, California Girls)
 Sample Edit](https://youtu.be/mSJosmuG-H0)__
## Get It

Clone the project

```bash
  git clone https://github.com/hari01584/beat-remix
```

Go to the project directory

```bash
  cd beat-remix
```

Install requirements

```bash
  pip install -r requirements.txt
```

run the main script

```bash
  python beat.py
```

_Note: You also need ffmpeg to run BeatRemix, [follow this tutorial](https://www.videoproc.com/resource/how-to-install-ffmpeg.htm) and get it installed._
## Usage/Examples

How to use?

1. Place all Image files in _images/[directory]/_ folder.
2. Place sound files in _sounds/_ folder.
3. Call _python beat.py_ and select _image directory and sound file upon prompt._

__Note: There is already starter files for both images and sounds in project, so you can directly call beat.py and choose upon existing default files!__
## FAQ

#### Is it good for production level?

BeatRemix is just a proof-of-concept work to demonstrate the future possibilities of automatically editing videos but currently it cannot be used as production ready application, since the video lacks many important things like filters/transitions etc!

#### Can we use it without any video editing skills?

Obviously duh, that's why it's made!
## Contributing

Contributions are always welcome, for starters you can see into beats.py that contains source code to call SimpleBeatButter and SimpleHoneyMerger classes, these classes contains the groundwork of splitting/analyzing/merging images with sound! You can create more such classes by following the template and make pull requests here!

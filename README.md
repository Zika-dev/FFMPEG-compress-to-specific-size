# FFMPEG-compress-to-specific-size
I made this a while ago so the code is not very good, but it seems to be working decently.

# How to use

- Run main.py
- Select input video
- Select starting bitrate
- Enter desired file size
- Wait...
- File will be outputted as "output.mp4"

# Warning

I have noticed that it's not very accurate.
### Example: When i want to compress something to 50mb, the file size may be compressed to 40-45mb. I can probably fix this but it's gonna take a longer time to render the video

# Requirements

- Python 3.1<
- FFMPEG
- tkinter
- subprocess
- tqdm

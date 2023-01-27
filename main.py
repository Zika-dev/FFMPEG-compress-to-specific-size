import os
import ffmpeg
import tkinter as tk
import subprocess
from tqdm import tqdm
from tkinter import filedialog

print("NOTE: File name may not involve spaces!")

# Choose file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir="C:", title="Select a video", filetypes=(("mp4", "*.mp4"), ))

input_file = file_path
print(input_file)
output_file = 'output.mp4'

# Find resolution and bitrate
video = ffmpeg.input(input_file)
video_info = ffmpeg.probe(input_file)

height = video_info['streams'][0]['height']
width = video_info['streams'][0]['width']
res = str(width) + " " + str(height)
print("Resolution: "  + str(res))

# Get input size
inSize = os.path.getsize(input_file)

def get_bitrate(video_file):
    command = ["ffprobe", "-v", "error", "-show_entries",
               "format=bit_rate", "-of", "default=noprint_wrappers=1:nokey=1", video_file]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return int(result.stdout)

def compress(video_file):
    command2 = ("ffmpeg -i " + input_file + " -b " + str(bitrate) + " " + output_file)
    result = subprocess.run(command2, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return (result.stdout)
    print("Done")

def_bitrate = get_bitrate(input_file)
print(f"Bitrate: " + str(def_bitrate))

# Script needs an output file to work
try:
    outSize = os.path.getsize("output.mp4")
except WindowsError as outSize:
    print("Failed to find output an output file... Creating a new one")
    f = open("output.mp4", "x")
    f.close()

# Input bitrate
while True:
    bitrate = input("How much do you want the starting bitrate to be? (Leave blank to use video bitrate *RECOMMENDED*) ")
    if bitrate == '':
        bitrate = def_bitrate
        break
    try:
        bitrate = int(bitrate)
    except ValueError as bitrate:
        print("Enter a valid number! ")
    else:
        break

print("Bitrate Set to: " + str(bitrate))

# Input desired size
while True:
    size = input("Enter desired file size in MBs: ")
    try:
        size = int(size)
    except ValueError as size:
        print("Enter a valid number! ")
    else:
        break

bitrate = int(bitrate)

outSize = os.path.getsize("input.mp4")
os.path

# Estimate time
outSize2 = inSize/1000000
index = []
while outSize2 > int(size):
    outSize2 *= 0.8
    index.append(outSize2)

# Calculate progress bar length
change_fac = round(outSize2 / (inSize/1000000), 2)
print(change_fac)
bitrate = bitrate*change_fac

x = int(len(index))
x /= 10
if isinstance(x, float):
    x += 1
in_x = int(x)

print("Estimated iterations: ~" + str(in_x))

pbar = tqdm(total=int(x))

# Compress the video
while outSize > int(size):
    os.remove("output.mp4")
    def_compress = compress(input_file)
    outSize = os.path.getsize("output.mp4")
    outSize = outSize / 1000000
    outSize = round(outSize, 2)

    # Calculate next bitrate attempt
    if int(outSize) / int(size) >= 2:
        bitrate *= 0.25
    elif int(outSize) / int(size) >= 1:
        bitrate *= 0.5
    else:
        bitrate *= 0.8
    pbar.update(1)

# Done
else:
    os.system('cls')
    if outSize <= 0:
        print("Failed! Final video is too small. Try setting your desired size to a higher amount.")
    else:
        print("Success!\n")
        print("Final size: ", str(outSize)+"Mb\n" + "Bitrate: " + str(bitrate))
    os.system("pause")
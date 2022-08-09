import moviepy.editor as mpy
from tkinter.filedialog import *

vid = askopenfilename()
video = mpy.VideoFileClip(vid)

audio = video.audio
audio.write_audiofile("audio.mp3")  

print("Done!")
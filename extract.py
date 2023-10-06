from moviepy.editor import *
from pygemstones.util import log as l

# setup
l.d("Starting...")

# load the video from which the audio will be extracted
video = VideoFileClip("temp/movie.mp4")

# extract audio from the video
audio = video.audio

# save the audio in a temporary format (in this case, mp3)
audio.write_audiofile("temp/audio.mp3")

l.s("Audio extracted and saved to temp/audio.mp3")

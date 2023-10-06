from textwrap import wrap

import numpy as np
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from PIL import Image, ImageDraw, ImageFont
from pygemstones.util import log as l


# custom generator function
def generator(txt):
    wrapped_txt = "\n".join(wrap(txt, width=20))
    wrapped_txt = wrapped_txt.upper()

    # create a PIL image with an alpha channel (RGBA)
    img = Image.new("RGBA", (video.size[0], int(video.h * 0.2)), color=(0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, fontsize)

    # calculate text size and position
    left, top, right, bottom = d.multiline_textbbox((0, 0), wrapped_txt, font=font)
    text_width, text_height = right - left, bottom - top
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2

    # draw the text with a border
    for i in range(-border_thickness, border_thickness + 1):
        for j in range(-border_thickness, border_thickness + 1):
            d.multiline_text(
                (x + i, y + j),
                wrapped_txt,
                font=font,
                fill=border_color,
                align="center",
            )

    # draw the text in yellow
    d.multiline_text((x, y), wrapped_txt, font=font, fill="yellow", align="center")

    # convert the PIL image to a NumPy array
    img_np = np.array(img)

    # convert the NumPy array to a video clip
    return ImageClip(img_np)


# setup
l.d("Starting...")

# load your video
video = VideoFileClip("temp/movie.mp4")

# calculate the font size as 4% of the video's height
fontsize = int(video.h * 0.04)

# font path
font_path = "fonts/Montserrat-Black.ttf"

# border settings
border_thickness = 8
border_color = "black"

# read the transcript file and create a subtitle object
l.d(f"Generating subtitles...")
subtitles = SubtitlesClip("temp/transcript.txt", generator)

# position the subtitles on the video, aligned at the bottom
l.d(f"Setup subtitles...")
subtitles = subtitles.set_pos(("center", "bottom"))

# start at the beginning of the video
subtitles = subtitles.set_start(0)

# duration of subtitles inside the video
subtitles = subtitles.set_duration(video.duration)

# place the subtitles 12% above the video's bottom
subtitles = subtitles.margin(bottom=int(video.h * 0.12), opacity=0)

# add the subtitles to the original video
l.d(f"Mixing video and subtitles...")
final_video = CompositeVideoClip([video, subtitles])

# add the original audio to the video
l.d(f"Adding original audio...")
final_video.audio = video.audio

# export the final video
l.d(f"Exporting final video...")

final_video.write_videofile(
    "temp/movie-out.mp4",
    fps=video.fps,
    codec="libx264",
    audio_codec="mp3",
)

l.s("Exported to temp/movie-out.mp4")

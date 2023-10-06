import os

import assemblyai as aai
from pygemstones.util import log as l


# function to format time
def format_time(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


# setup
l.d("Starting...")

aai.settings.api_key = os.environ["ASSEMBLYAI_KEY"]
subtitle_words = 5
audio_file = "temp/audio.mp3"
transcript_file = "temp/transcript.txt"

# transcribe audio
l.d("Transcribing audio...")

config = aai.TranscriptionConfig(language_code=aai.LanguageCode.pt)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_file, config)

with open(transcript_file, "w", encoding="utf-8") as file:
    l.d("Writing subtitles...")

    srt_string = ""
    subtitle_count = 1
    buffer = []

    # initialize previous end time as 0
    previous_end_time = 0

    for word in transcript.words:
        text = word.text

        # start time is the same as the previous end time
        start_time = previous_end_time
        end_time = word.end

        buffer.append(text)

        if len(buffer) == subtitle_words:
            srt_string += f"{subtitle_count}\n"
            srt_string += f"{format_time(start_time)} --> {format_time(end_time)}\n"
            srt_string += " ".join(buffer) + "\n\n"

            subtitle_count += 1
            buffer = []

            # update previous time to keep it showing
            previous_end_time = end_time

    # check if still words in the buffer
    if buffer:
        srt_string += f"{subtitle_count}\n"
        srt_string += f"{format_time(previous_end_time)} --> {format_time(end_time)}\n"
        srt_string += " ".join(buffer) + "\n\n"

    file.write(srt_string)

l.s(f"Subtitles saved in {transcript_file}")

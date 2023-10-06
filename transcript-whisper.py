from pygemstones.io import file as f
from pygemstones.system import runner as r
from pygemstones.util import log as l

# sample from cmd line:
# whisper temp/audio.mp3 --language pt --word_timestamps True --model medium --output_dir temp/transcript --max_line_width 20 --max_line_count 2
# whisper-ctranslate2 temp/audio.mp3 --word_timestamps True --model medium --output_dir temp/transcript --max_line_width 20 --max_line_count 2

# whisper python lib: openai-whisper
# fast whisper python lib: whisper-ctranslate2

# setup
l.d("Starting...")

subtitle_words = 5
audio_file = "temp/audio.mp3"
transcript_file = "temp/transcript.txt"
whisper_transcript_file = "temp/transcript/audio.srt"
program = "whisper-ctranslate2"

# transcribe audio
l.d("Transcribing audio...")

r.run(
    [
        program,
        "temp/audio.mp3",
        "--word_timestamps",
        "True",
        "--model",
        "medium",
        "--output_dir",
        "temp/transcript",
        "--max_line_width",
        "20",
        "--max_line_count",
        "2",
        "--suppress_tokens",
        "0,11,13,30",
    ],
)

f.copy_file(whisper_transcript_file, transcript_file)

l.s(f"Subtitles saved in {transcript_file}")

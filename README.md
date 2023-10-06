# PyTranscriptorAi - Transcript videos to text with Ai and add subtitles

[![Movie Generated From Ai](https://github.com/paulocoutinhox/py-transcriptor-ai/actions/workflows/build.yml/badge.svg)](https://github.com/paulocoutinhox/py-transcriptor-ai/actions/workflows/build.yml)

This is a nice software that generate subtitles for a video using Ai.

What is included in my process:

- MoviePy to extract the audio from video
- A service to transcript the video to text (speech to text)
- A small logic to generate subtitles in a nice way
- MoviePy to add subtitles to video and generate final movie
- Video is built and released from Github CI/CD (actions)

## How to install

1. Python3: `https://www.python.org/`
2. ImageMagick: `https://imagemagick.org/`
3. Python dependencies: `python3 -m pip install -r requirements.txt`

## How to use with Whisper

Install the Whisper dependencies: `python3 -m pip install whisper-ctranslate2`.

Copy your video to path: `temp/movie.mp4`.

Run in terminal these three commands for each time that your need add subtitles to your file `temp/movie.mp4`:

```
python3 extract.py
python3 transcript-whisper.py
python3 generate.py
```

## How to use with AssemblyAi

Install the AssemblyAi dependencies: `python3 -m pip install assemblyai`.

Get a key for AssemblyAi API: `https://www.assemblyai.com/`.

Add the key for AssemblyAi to your environment variable `ASSEMBLYAI_KEY`:

```
export ASSEMBLYAI_KEY="your-key-here"
```

Copy your video to path: `temp/movie.mp4`.

Run in terminal these three commands for each time that your need add subtitles to your file `temp/movie.mp4`:

```
python3 extract.py
python3 transcript-assemblyai.py
python3 generate.py
```

## Sample

https://github.com/paulocoutinhox/py-transcriptor-ai/assets/395096/eafa7385-1fdd-447f-9711-210c3b722d3c

## Speed up video

If you need speed up your final video file, install `ffmpeg`` and run one of these commands for the desired speed:

**Speed 1.2:**

```
ffmpeg -i temp/movie-out.mp4 -filter_complex "[0:v]setpts=0.8333*PTS[v];[0:a]atempo=1.2[a]" -map "[v]" -map "[a]" -c:a mp3 temp/movie_1_2x_with_audio.mp4
```

**Speed 1.5:**

```
ffmpeg -i temp/movie-out.mp4 -filter_complex "[0:v]setpts=0.6667*PTS[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" -c:a mp3 temp/movie_1_5x_with_audio.mp4
```

**Speed 1.75:**

```
ffmpeg -i temp/movie-out.mp4 -filter_complex "[0:v]setpts=0.5714*PTS[v];[0:a]atempo=1.75[a]" -map "[v]" -map "[a]" -c:a mp3 temp/movie_1_75x_with_audio.mp4
```

**Speed 2.0:**

```
ffmpeg -i temp/movie-out.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" -c:a mp3 temp/movie_2x_with_audio.mp4
```

<div align="center">

# PROTUBE

### A simple, powerful YouTube downloader for your terminal.

**Download audio, videos, and entire playlists with a single command.**

`Python` · `yt-dlp` · `FFmpeg` · `CLI`

[Features](#features) · [Installation](#installation) · [Usage](#usage) · [Options](#command-line-options) · [Notes](#important-notes)

</div>

---

## Overview

**ProTube** is a lightweight Python command-line interface built around [yt-dlp](https://github.com/yt-dlp/yt-dlp). It provides straightforward commands for downloading YouTube content as MP3 audio or video, with optional quality settings, playlist support, and custom output directories.

No complex setup, no graphical interface. Just your terminal.

## Features

- **Audio downloads**: Extract audio and convert it to MP3.
- **Video downloads**: Download video streams with a selectable maximum resolution.
- **Playlist support**: Download an entire playlist when requested.
- **Quality controls**: Choose from documented audio bitrates and video resolutions.
- **Custom output folders**: Keep downloads wherever you prefer.
- **Metadata and thumbnails**: Request embedded metadata and thumbnails through `yt-dlp`.
- **Organized filenames**: Include uploader and title, plus playlist position for playlist downloads.
- **Cross-platform Python script**: Designed to run from a terminal on Windows, macOS, or Linux when the required tools are available.

## Requirements

Make sure the following are installed:

- **Python 3**
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**, available as the `yt-dlp` command on your `PATH`
- **[FFmpeg](https://ffmpeg.org/)** (including `ffprobe`), available on your `PATH` for audio conversion, merging, and media embedding

You can install `yt-dlp` with:

```bash
python -m pip install -U yt-dlp
```

Verify that the external commands are available:

```bash
yt-dlp --version
ffmpeg -version
```

> **Note:** The script launches `yt-dlp` as an external executable, so installing the Python package alone is not enough unless the `yt-dlp` command is also accessible on your `PATH`.

## Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/unicodeces/ProTube.git
cd ProTube
```

Or download the repository as a ZIP and extract it.

> Replace `unicodeces` with the GitHub account hosting the project.

## Usage

### Download audio (MP3)

```bash
python run.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

By default, ProTube requests MP3 at **320 kbps** and saves files in `musicas/`.

### Choose audio quality

```bash
python run.py -q 192 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Supported documented values: `320`, `192`, `128` (kbps).

### Download video

```bash
python run.py -v "https://www.youtube.com/watch?v=VIDEO_ID"
```

By default, ProTube selects streams up to **1080p** and saves files in `videos/`.

### Choose video resolution

```bash
python run.py -v -q 720 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Supported documented values: `1080`, `720`, `480` (maximum height in pixels).

### Use a custom output directory

```bash
python run.py -v -q 720 -o downloads "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Download an entire playlist

Audio playlist:

```bash
python run.py -p "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

Video playlist:

```bash
python run.py -p -v -q 720 "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

**Tip:** Use quotes around URLs, especially when they contain `&` or other shell-special characters.

## Command-line options

| Option | Description |
| :-- | :-- |
| `-h`, `--help` | Show the built-in help message. |
| `-o`, `--output DIR` | Set a custom output directory. |
| `-q`, `--quality VALUE` | Set audio bitrate or maximum video resolution. |
| `-v`, `--video` | Download video instead of extracting MP3 audio. |
| `-p`, `--playlist` | Download the full playlist instead of a single item. |

### Default settings

| Setting | Audio mode | Video mode |
| :-- | :-- | :-- |
| Output folder | `musicas/` | `videos/` |
| Quality setting | `320` kbps | Up to `1080`p |
| Format | MP3 | Video streams merged to MP4 when applicable |
| Playlist download | Off | Off |

## Output filenames

Individual downloads use:

```text
Uploader - Title.ext
```

Playlist downloads use:

```text
PlaylistIndex - Uploader - Title.ext
```

The output directories are created automatically if they do not already exist (for standard single-level directory paths).

## Important notes

- **Source quality matters.** Converting audio to 320 kbps MP3 does not improve the quality of the original YouTube audio stream.
- **Resolution is a ceiling, not a guarantee.** If the selected resolution is unavailable, `yt-dlp` may choose a lower-quality format.
- **MP4 compatibility can vary.** The script requests MP4 as the merge container, but actual codecs and whether merging occurs depend on the downloaded streams and FFmpeg.
- **YouTube changes frequently.** Keep `yt-dlp` up to date if extraction stops working.
- **Platform restrictions apply.** Availability and download success depend on the content, YouTube's behavior, and your environment.

## Troubleshooting

**`yt-dlp` command not found**

Install `yt-dlp` and ensure its executable directory is included in your system `PATH`.

**FFmpeg errors**

Install FFmpeg and confirm that both `ffmpeg` and `ffprobe` can be called from your terminal.

**Download fails or a format is unavailable**

Update `yt-dlp`, check the URL, and try a different quality setting. Some videos or formats may be inaccessible.

## Responsible use

Download only content you have the right or permission to download. Respect copyright, applicable laws, and the terms of the services you use. PROTUBE is an independent wrapper around `yt-dlp` and is not affiliated with YouTube or Google.

## Credits

Built with [Python](https://www.python.org/) and powered by the open-source [yt-dlp](https://github.com/yt-dlp/yt-dlp) project and [FFmpeg](https://ffmpeg.org/).

---

<div align="center">

**ProTube** · Simple commands. Your media. Your terminal.

</div>

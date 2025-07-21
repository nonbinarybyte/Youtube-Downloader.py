import argparse
import subprocess
from pathlib import Path

def download(url, output_path, audio_only):
    folder = Path(output_path)
    folder.mkdir(parents=True, exist_ok=True)

    command = [
        "yt-dlp",
        url,
        "-o", f"{folder}/%(playlist_index)s - %(title).80s.%(ext)s",
    ]

    if audio_only:
        command += [
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "192K",
        ]

    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="URL of a single video")
    parser.add_argument("--playlist", help="URL of a playlist")
    parser.add_argument("--audio-only", action="store_true", help="Download as audio only")
    parser.add_argument("--output", default="downloads", help="Output folder")
    args = parser.parse_args()

    url = args.video or args.playlist
    if not url:
        print("You must provide either --video or --playlist")
        return

    download(url, args.output, args.audio_only)

if __name__ == "__main__":
    main()

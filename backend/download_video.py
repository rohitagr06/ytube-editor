# backend/download_video.py

import os
from yt_dlp import YoutubeDL
from datetime import datetime

# This function downloads a YouTube video and returns the final saved file path.
def download_video(url: str, output_dir: str = "output") -> str:
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Format timestamp to append in filename to avoid overwriting
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'%(title)s_{timestamp}.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
    }

    # Download video using yt-dlp
    with YoutubeDL(ydl_opts) as ydl:
        print(f"⏬ Downloading from YouTube: {url}")
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)

        # Convert file extension to .mp4 if not already
        if not filename.endswith('.mp4'):
            filename = filename.rsplit('.', 1)[0] + '.mp4'

        print(f"✅ Downloaded video to: {filename}")
        return filename
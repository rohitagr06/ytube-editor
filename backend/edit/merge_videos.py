from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from datetime import datetime

def merge_videos(file_paths):
    """
    Merge multiple video files into one.

    Args:
        file_paths (list): List of paths to the video files to be merged.

    Returns:
        str: Path to the merged video.
    """
    clips = [VideoFileClip(f) for f in file_paths]
    final_clip = concatenate_videoclips(clips)

    # Save with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join("output", "merge")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"merged_{timestamp}.mp4")

    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
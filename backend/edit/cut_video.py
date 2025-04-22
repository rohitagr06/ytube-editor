from moviepy.editor import VideoFileClip
import os
from datetime import datetime

def cut_video(input_path, start_time, end_time):
    """
    Cut the video between start_time and end_time and save it with a timestamped filename.
    
    Args:
        input_path (str): Path to the input video.
        start_time (str): Start time in 'mm:ss' or 'hh:mm:ss' format.
        end_time (str): End time in 'mm:ss' or 'hh:mm:ss' format.
    
    Returns:
        str: Path to the output cut video.
    """
    video = VideoFileClip(input_path).subclip(start_time, end_time)

    # Save with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join("output", "cut")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"cut_{timestamp}.mp4")

    video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path
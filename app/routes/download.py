from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
import sys
# Add backend folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../backend")))
from download_video import download_video

download_bp = Blueprint('download', __name__)

@download_bp.route('/', methods=['GET', 'POST'])  # This will be accessed via /download
def download():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if not video_url:
            flash("⚠️ Please provide a YouTube link.", "error")
            return redirect(url_for('download.download'))

        try:
            # Call your existing download function
            downloaded_path = download_video(video_url, download_type='video')
            flash(f"✅ Download complete! File saved to: {downloaded_path}", "success")
        except Exception as e:
            flash(f"❌ Error during download: {str(e)}", "error")

        return redirect(url_for('download.download'))

    return render_template('download.html')
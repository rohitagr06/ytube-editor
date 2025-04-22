from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
import sys
from werkzeug.utils import secure_filename
from datetime import datetime

# Add backend/edit path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../backend/edit')))
from cut_video import cut_video
from merge_videos import merge_videos

edit_bp = Blueprint('edit', __name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@edit_bp.route('/cut', methods=['GET', 'POST'])
def cut():
    if request.method == 'POST':
        video = request.files.get('video')
        start = request.form.get('start_time')
        end = request.form.get('end_time')

        if not video or not start or not end:
            flash("⚠️ Please upload a video and enter start and end times.", "error")
            return redirect(url_for('edit.cut'))

        filename = secure_filename(video.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        video.save(input_path)

        try:
            output_path = cut_video(input_path, start, end)
            flash(f"✅ Video cut successfully: {output_path}", "success")
        except Exception as e:
            flash(f"❌ Error: {str(e)}", "error")

        return redirect(url_for('edit.cut'))

    return render_template('cut.html')


@edit_bp.route('/merge', methods=['GET', 'POST'])
def merge():
    if request.method == 'POST':
        videos = request.files.getlist('videos')
        file_paths = []

        if not videos or len(videos) < 2:
            flash("⚠️ Please upload at least two videos to merge.", "error")
            return redirect(url_for('edit.merge'))

        for video in videos:
            filename = secure_filename(video.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            video.save(path)
            file_paths.append(path)

        try:
            output_path = merge_videos(file_paths)
            flash(f"✅ Videos merged successfully: {output_path}", "success")
        except Exception as e:
            flash(f"❌ Error: {str(e)}", "error")

        return redirect(url_for('edit.merge'))

    return render_template('merge.html')
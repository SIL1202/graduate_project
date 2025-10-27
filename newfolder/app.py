from flask import Flask, render_template, request, send_from_directory
import os
import subprocess
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
RESULT_FOLDER = os.path.join('static', 'results')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER


@app.route('/')
def index():
    return render_template('index.html', video_path=None)


@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files.get('video')
    if not file or file.filename == '':
        return "沒有選擇影片"

    # 儲存原始影片
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(original_path)

    # 生成轉檔後檔名
    base_name = os.path.splitext(file.filename)[0]
    output_filename = f"{base_name}_converted_{datetime.now().strftime('%H%M%S')}.mp4"
    output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)

    # 使用 ffmpeg 轉成瀏覽器可播放格式
    # libx264 → H.264 影像, aac → 音訊
    try:
        subprocess.run([
            "ffmpeg", "-y",
            "-i", original_path,
            "-vcodec", "libx264",
            "-acodec", "aac",
            "-movflags", "faststart",
            output_path
        ], check=True)
    except subprocess.CalledProcessError:
        return "轉檔失敗，請確認是否已安裝 ffmpeg"

    return render_template('index.html', video_path=f"results/{output_filename}")


@app.route('/results/<filename>')
def result_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
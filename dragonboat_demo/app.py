from flask import Flask, render_template, request, redirect, url_for
import os
from ultralytics import YOLO
import shutil
import time

app = Flask(__name__)

# 設定上傳與輸出資料夾
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# 載入 YOLO 模型
MODEL_PATH = 'best.pt'
model = YOLO(MODEL_PATH)
print(f"✅ 模型已載入：{MODEL_PATH}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "沒有上傳影片"

    file = request.files['video']
    if file.filename == '':
        return "沒有選擇影片"

    # 儲存上傳影片
    video_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(video_path)

    # 執行 YOLO 偵測
    print(f"🎬 開始分析影片：{video_path}")
    results = model.predict(source=video_path, save=True, project='runs/detect', name='web_predict', exist_ok=True)

    # 找到 YOLO 的輸出影片
    output_dir = 'runs/detect/web_predict'
    result_video_path = os.path.join(output_dir, file.filename)
    final_path = os.path.join(RESULT_FOLDER, file.filename)

    # 移動 YOLO 輸出到 static/results
    if os.path.exists(result_video_path):
        shutil.move(result_video_path, final_path)
        print(f"✅ 偵測完成，輸出影片：{final_path}")
    else:
        print("❌ 沒有找到 YOLO 輸出影片")

    # 回傳可播放影片
    return render_template('index.html', result_video=url_for('static', filename=f'results/{file.filename}'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
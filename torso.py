# This file aims to export the video with the body being boxed and showing the struture of the torso.
from ultralytics import YOLO

# load a pretrained model (recommended for training)
model = YOLO("yolo11n-pose.pt")

results = model.predict(source="source.mp4", show=True, save=True)

# Dragon Boat Motion Analysis Project

## Project Overview

This graduate project focuses on **motion analysis for dragon boat athletes** using **computer vision and deep learning**. The main goal is to **analyze paddle motion** and **quantify key performance metrics** (such as stroke frequency, stroke distance, entry/exit angles, and velocity) through **video-based detection and tracking**.

The project combines **YOLO-based paddle detection**, **pose estimation**, and **data analysis** to support **coaches, athletes, and researchers** in understanding paddling techniques more precisely.

---

## Repository Structure

* `clip.py` — Extracts frames or clips from raw videos for dataset creation.
* `check_dataset.py` — Verifies image-label consistency in training and validation sets.
* `make_val_split.py` — Automatically splits training data into training and validation sets.
* `torso.py` — Contains torso and paddle detection logic for pose alignment and motion segmentation.
* `predict.sh` — Runs YOLO model inference on videos to generate predictions.
* `train_and_predict.sh` — Full pipeline for model training and prediction in a single script.
* `requirements.txt` — Lists all dependencies required to run the project.

---

## Model Development

### YOLOv11 Paddle Detection

We trained multiple iterations of YOLO models for **paddle position detection**:

* **Second version** → First YOLO training attempt.
* **Third version** → Refined dataset with 912 labeled images.

Training and validation data were prepared and uploaded to **Roboflow** for **auto-labeling** and dataset management.

### 2D Human Pose Estimation

Based on the slides in `724龍舟.pptx`, the project also explored **human pose estimation** for analyzing upper-body motion:

* **Top-down approach** using YOLO + ViTPose / HRNet.
* **Focus**: Detect wrist and arm movement to infer paddle motion.
* **Alternative methods**: Direct paddle detection vs inferred paddle estimation using pose keypoints.

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Check dataset consistency

```bash
python3 check_dataset.py
```

### 3. Split the data set

```bash
python3 make_val_split.py
```

### 4. Train the YOLO model

```bash
bash train.sh
```

---

## Research Background

Reference material from the **Sports Science & Technology Center (運動科學與科技中心)** presentation outlines real-world metrics in dragon boat racing, including:

* Stroke frequency (spm)
* Stroke distance (cm)
* Entry, exit, and maximum angles (degrees)
* Stroke duration and recovery time (ms)

The model aims to extract similar measurements **automatically from video footage**.

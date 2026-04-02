#  Helmet & Number Plate Detection System

##  Project Overview

This project detects:

* Helmet / No Helmet 
* Number Plates 

using **YOLOv5 (Object Detection)** and real-time webcam/video input.

---

## Features

* Real-time detection using webcam
* Detects helmet violations
* Can be extended to extract number plates (OCR)
* Works on images, videos, and live camera

---

##  Technologies Used

* Python
* OpenCV
* PyTorch
* YOLOv5 (Ultralytics)

---

##  Project Structure

```
HelmetAndNumber/
│── yolov5/                # YOLOv5 repository
│── last.pt               # Trained custom model
│── yolov5.py             # Detection script (optional)
│── README.md
```

---

##  Installation

### 1. Clone YOLOv5

```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### 2. Install Dependencies

```
pip install torch torchvision torchaudio
pip install opencv-python
```

---

##  Run the Project

### Run with Webcam

```
python detect.py --weights ../last.pt --source 0
```

### Run with Image

```
python detect.py --weights ../last.pt --source path/to/image.jpg
```

### Run with Video

```
python detect.py --weights ../last.pt --source path/to/video.mp4
```

---

##  Model Details

* Model: YOLOv5 Custom Trained Model
* Classes:

  * Helmet
  * No Helmet
  * Number Plate

---

## 📸 Sample Output

* Detects riders with/without helmets
* Highlights number plates

---

## Limitations

* Accuracy depends on training dataset
* Low-light detection may be weak

---

##  Future Enhancements

* Number plate text extraction (OCR)
* Fine/penalty system
* Web app using Streamlit
* Database integration

---

##  Author

Bongu Venkatesh

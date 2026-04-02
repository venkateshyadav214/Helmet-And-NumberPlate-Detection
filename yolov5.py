import torch
import numpy as np
import cv2

from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov5s.pt")   # OR use "last.pt" for helmet detection

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Camera not working")
        break

    results = model(frame)

    annotated_frame = results[0].plot()
    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

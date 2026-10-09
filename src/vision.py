import os
import urllib.request
import cv2
from ultralytics import YOLO
from PIL import Image

MODEL_URL = "https://huggingface.co/baskarmother/yolov8-ppe-construction/resolve/main/best.pt"
MODEL_PATH = "yolov8_ppe.pt"

def load_yolo_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading YOLOv8 PPE model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    return YOLO(MODEL_PATH)

def detect_ppe(image: Image.Image):
    model = load_yolo_model()
    results = model.predict(source=image, conf=0.40)
    
    # YOLO plot returns BGR format; convert to RGB for natural colors
    annotated_bgr = results[0].plot()
    annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
    
    detected_classes = [model.names[int(box.cls[0])] for box in results[0].boxes]
    return annotated_rgb, detected_classes
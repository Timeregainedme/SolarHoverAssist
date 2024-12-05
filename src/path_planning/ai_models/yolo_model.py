import torch
from pathlib import Path

def load_yolo_model(model_path):
    if not Path(model_path).exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
    return model

if __name__ == "__main__":
    model = load_yolo_model("models/best.pt")
    print("YOLO model loaded successfully.")

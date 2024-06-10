import os

from ultralytics import YOLO

MODEL_DIR_PATH = "/content/drive/MyDrive/Colab Notebooks/model"
DATASET_DIR_PATH = "/content/drive/MyDrive/Colab Notebooks/dataset/"

model = YOLO(os.path.join(MODEL_DIR_PATH, "yolov8n.yaml")).load(
    os.path.join(MODEL_DIR_PATH, "yolov8n.pt")
)

results = model.train(
    data=os.path.join(DATASET_DIR_PATH, "data.yaml"),
    imgsz=640,
    epochs=50,
    batch=32,
    device=0,
)

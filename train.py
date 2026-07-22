from ultralytics import YOLO

def main():
    model = YOLO("yolov8m.pt")  # 25.9M parámetros

    results = model.train(
        data="datasets/data.yaml",
        epochs=100,
        imgsz=640,
        batch=8,
        optimizer="Adam",
        lr0=0.001,
        device="0",
        name="Hand_Detection",
        save=True,
        save_period=10,
        save_json=True,
        project="runs",
        exist_ok=True,
        resume=False,
        patience=10,
    )

if __name__ == "__main__":
    main()
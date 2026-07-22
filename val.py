from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/train/weights/best.pt")

    metrics = model.val(
        data="datasets/data.yaml",
        split="val",
        imgsz=640,
        conf=0.9,
        iou=0.6,
        device="0",
    )
    print(metrics.results_dict)

if __name__ == "__main__":
    main()
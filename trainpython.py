from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(
    data=r"E:\naan_mudhalvan\hackathon\NAANMUDHALVAN_HACKATHON\battery_defect_detector.v4i.yolov8\data.yaml",  # Ensure this path is correct
    epochs=50,
    imgsz=640,
    batch=8,
    name="battery_defect_train",
    verbose=True  # Shows detailed progress
)

print("Training completed. Check 'runs/detect/battery_defect_train/' for best.pt")
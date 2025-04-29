from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Load your trained model
cap = cv2.VideoCapture(1)  # Webcam

while True:
    ret, frame = cap.read()
    results = model.predict(frame, conf=0.7)  # Detect defects
    annotated_frame = results[0].plot()  # Draw boxes
    cv2.imshow("Battery Defect Detector", annotated_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
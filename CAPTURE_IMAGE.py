import cv2
import os

# Set save path
save_path = os.path.join(os.getcwd(), "IMAGES", "Battery")
os.makedirs(save_path, exist_ok=True)

# Open webcam
cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image.")
        break

    cv2.imshow("Webcam - Press 's' to save, 'q' to quit", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):  # Press 's' key to save image
        img_name = f"battery_{count}.jpg"
        cv2.imwrite(os.path.join(save_path, img_name), frame)
        print(f"Saved: {img_name}")
        count += 1

    elif key == ord('q'):  # Press 'q' key to quit
        break

cap.release()
cv2.destroyAllWindows()

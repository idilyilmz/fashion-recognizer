import cv2
import os
from pathlib import Path

def blur_faces(image_path, output_path):
    """Detect and blur faces for ethical compliance."""
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face_region = img[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face_region, (99, 99), 30)
        img[y:y+h, x:x+w] = blurred

    cv2.imwrite(output_path, img)

def process_folder(input_dir, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    for fname in os.listdir(input_dir):
        if fname.lower().endswith((".jpg", ".jpeg", ".png")):
            blur_faces(
                os.path.join(input_dir, fname),
                os.path.join(output_dir, fname)
            )
            print(f"Processed: {fname}")

if __name__ == "__main__":
    process_folder("data/raw/campus_photos", "data/processed")
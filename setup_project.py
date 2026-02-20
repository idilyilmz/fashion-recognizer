import os

folders = [
    "data/raw/campus_photos",
    "data/raw/videos",
    "data/annotated/images/train",
    "data/annotated/images/val",
    "data/annotated/images/test",
    "data/annotated/labels/train",
    "data/annotated/labels/val",
    "data/annotated/labels/test",
    "data/processed",
    "models/pretrained",
    "models/trained",
    "src",
    "notebooks",
    "outputs/detections",
    "outputs/logs",
    "outputs/charts",
    "configs",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

# Create placeholder files
open("src/__init__.py", "w").close()
print("Project structure ready!")
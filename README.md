# Real-Time Object Detection

A small learning project using Python, OpenCV, and YOLO. It can show a webcam preview and detect common objects with labels and boxes.

## Setup

Use Python 3.12. Open PowerShell in this project folder and run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run live detection

```powershell
.\.venv\Scripts\python.exe src\object_detection\live_detection.py
```

Press **q** in the webcam window to close it. The first run may download the YOLO model file automatically.

## Project files

- `src/object_detection/live_detection.py` — detects objects from the webcam.
- `src/object_detection/detect_image.py` — detects objects in an image. Add your own image under `data/samples/` and update `image_path` in the file before running it.
- `src/object_detection/webcam_viewer.py` — displays the webcam without detection.
- `src/object_detection/image_viewer.py` — opens a sample image.

The included YOLO model recognizes its trained object classes. It has not been trained to recognize a comb.

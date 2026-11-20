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

- `src/object_detection/live_detection.py` - detects objects from the webcam.
- `src/object_detection/detect_image.py` - detects objects in an image. Add your own image under `data/samples/` and update `image_path` in the file before running it.
- `src/object_detection/webcam_viewer.py` - displays the webcam without detection.
- `src/object_detection/image_viewer.py` - opens a sample image.

The included YOLO model recognizes its trained object classes. It has not been trained to recognize a comb.

## Train a custom detector

To detect a new object (for example, a comb), collect images of it in varied settings and annotate each object's bounding box with an annotation tool. Export the annotations in Ultralytics YOLO detection format. Keep similar frames from the same video together in either the training or validation split.

Use this folder layout:

```text
datasets/comb/
|-- images/
|   |-- train/
|   `-- val/
|-- labels/
|   |-- train/
|   `-- val/
`-- data.yaml
```

Every image should have a matching `.txt` file in the corresponding `labels` folder. Each line in a label file describes one object as `class_id x_center y_center width height`; the four box values are normalized from 0 to 1. For one class named `comb`, use class ID `0`.

Put this in `datasets/comb/data.yaml`:

```yaml
train: images/train
val: images/val
names:
  0: comb
```

From the project folder, start training with the pretrained lightweight model:

```powershell
.\.venv\Scripts\yolo.exe detect train model=yolo26n.pt data=datasets/comb/data.yaml epochs=100 imgsz=640
```

After training, load `runs/detect/train/weights/best.pt` in `live_detection.py` by changing the model line to `model = YOLO("runs/detect/train/weights/best.pt")`. The dataset and trained weights are local files; keep them out of GitHub unless you intend to share them.

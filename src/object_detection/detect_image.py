import cv2
from ultralytics import YOLO


model = YOLO("yolo26n.pt")
image_path = "data/samples/test2.jpg"
results = model.predict(image_path)
image = cv2.imread(image_path)

for box in results[0].boxes:
    class_id = int(box.cls[0])
    label = model.names[class_id]
    confidence = float(box.conf[0])
    coordinates = box.xyxy[0].tolist()

    box_width = coordinates[2] - coordinates[0]
    box_height = coordinates[3] - coordinates[1]
    print("Box size:", box_width, "x", box_height)

    print("Object:", label)
    print("Confidence:", confidence)
    print("Box coordinates:", coordinates)

    x1 = int(coordinates[0])
    y1 = int(coordinates[1])
    x2 = int(coordinates[2])
    y2 = int(coordinates[3])

    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 2)
    cv2.putText(
        image,
        f"{label} {confidence:.2f}",
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 255),
        2,
    )

cv2.imshow("OpenCV Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

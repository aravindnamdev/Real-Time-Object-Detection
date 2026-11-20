import cv2


image_path = "data/samples/test.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image.")
else:
    cv2.imshow("Bottle Test", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

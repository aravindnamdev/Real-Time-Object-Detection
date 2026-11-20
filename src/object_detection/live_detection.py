import cv2  # OpenCV reads the webcam and draws on images.
from ultralytics import YOLO  # Import the YOLO object detection model.

model = YOLO("yolo26n.pt")  # Load the trained YOLO model file.
camera = cv2.VideoCapture(0)  # Open the default webcam (camera number 0).

if not camera.isOpened():  # Check whether the webcam opened correctly.
    print("Could not open the webcam.")  # Tell us if the webcam is unavailable.
else:  # Run the detection code when the webcam is ready.
    print("Press q to close the window.")  # Tell us how to stop the program.

    while True:  # Repeat these steps to process live camera frames.
        success, frame = camera.read()  # Read one picture from the webcam.

        if not success:  # Check whether a picture was read successfully.
            print("Could not read a camera frame.")  # Show the camera read problem.
            break  # Stop the loop if there is no picture.

        results = model.predict(frame, verbose=False)  # Ask YOLO to find objects.

        for box in results[0].boxes:  # Handle each object YOLO found in this frame.
            class_id = int(box.cls[0])  # Get the number for the object's class.
            label = model.names[class_id]  # Turn that class number into a name.
            confidence = float(box.conf[0])  # Get how sure YOLO is about the object.
            coordinates = box.xyxy[0].tolist()  # Get the box's left, top, right, bottom points.

            x1 = int(coordinates[0])  # Convert the left point to a pixel number.
            y1 = int(coordinates[1])  # Convert the top point to a pixel number.
            x2 = int(coordinates[2])  # Convert the right point to a pixel number.
            y2 = int(coordinates[3])  # Convert the bottom point to a pixel number.

            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)  # Draw a pink box.
            cv2.putText(  # Put the object's name and confidence on the frame.
                frame,  # Choose the camera picture to draw on.
                f"{label} {confidence:.2f}",  # Show the name and confidence to 2 decimals.
                (x1, y1 - 10),  # Place the text just above the box.
                cv2.FONT_HERSHEY_SIMPLEX,  # Choose a simple text style.
                0.8,  # Set the text size.
                (255, 0, 255),  # Use the same pink color as the box.
                2,  # Set the text thickness.
            )  # Finish drawing the text.

        cv2.imshow("Live Detection", frame)  # Show the current frame in a window.

        if cv2.waitKey(1) & 0xFF == ord("q"):  # Check whether q was pressed.
            break  # Stop the loop when q is pressed.

    camera.release()  # Give the webcam back to Windows.
    cv2.destroyAllWindows()  # Close the OpenCV display window.
import cv2


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open the webcam.")
else:
    print("Press q to close the webcam window.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Could not read a frame from the webcam.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("My Camera", gray_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

# Import necessary libraries
from cvzone.FaceDetectionModule import FaceDetector  # Import the FaceDetector class from cvzone module
import cv2  # Import OpenCV library

# Create a VideoCapture object to capture video from the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Create an instance of the FaceDetector class
detector = FaceDetector()

# Infinite loop to continuously process frames from the camera
while True:
    # Read a frame from the video capture
    success, img = cap.read()

    # Use the detector to find faces in the current frame
    img, bboxs = detector.findFaces(img)

    # Check if any faces are detected
    if bboxs:
        # Extract information about the first detected face
        # bboxs is a list of dictionaries, and each dictionary contains information about a detected face
        bboxInfo = bboxs[0]  # Get the dictionary for the first detected face
        center = bboxInfo["center"]  # Get the center coordinates of the face

        # Draw a filled circle at the center of the detected face
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    # Display the modified image with detected faces and circles
    cv2.imshow("Image", img)

    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

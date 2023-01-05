import cv2
import sys

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

#This line sets the video source to the default webcam, which OpenCV can easily capture.
video_capture = cv2.VideoCapture(0)

while True:
#Here, we capture the video. The read() function reads one frame from the video source, which in this example is the webcam. This returns:
    # The actual video frame read (one frame on each loop)
    # A return code
# The return code tells us if we have run out of frames, which will happen if we are reading from a file. This doesn’t matter when reading from the webcam, since we can record forever, so we will ignore it.
    ret, frame = video_capture.read()
    #Here we convert the frame to grayscale. Many operations in OpenCV are done in grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


# This function detects the actual face and is the key part of our code, so let’s go over the options:
    # The detectMultiScale function is a general function that detects objects. Since we are calling it on the face cascade, that’s what it detects.
    # The first option is the grayscale image.
    # The second is the scaleFactor. Since some faces may be closer to the camera, they would appear bigger than the faces in the back. The scale factor compensates for this.
# The detection algorithm uses a moving window to detect objects. minNeighbors defines how many objects are detected near the current one before it declares the face found. minSize, meanwhile, gives the size of each window.
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
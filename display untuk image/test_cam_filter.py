"""tryng with cam"""

import cv2
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(1)

while True:
    #capture frame by frame 
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    #draw
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #display
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
    #when done
    video_capture.release()
    cv2.destroyAllWindows()

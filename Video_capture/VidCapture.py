import cv2 as cv
import os

# # membaca file image lalu object tersebut ditaruh dalam object img
# img = cv.imread(cv.samples.findFile("Video_capture\\batu.jpg"))

# # mengecek apakah image kosong atua tidak
# if img is None:
#     sys.exit("Cannot read the image") #keluar

# # menunjukkan hasil gambar
# cv.imshow("Image", img)
# k = cv.waitKey(0) # mengecek input

# if k == ord("s"):
#     # mengesave image
#    cv.imwrite("batuss.png", img)


cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Something went wrong")
    exit()

hsv = False

while True:
    # capture frame by frame
    ret, frame = cam.read()

    # if frame is read correctly ret will be true
    if not ret:
        print("cant receive frame. stop video")
        break

    ## our operation on the frame come here
    # if cv.waitKey(2) == ord('r'):
    #     if not hsv:
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #     hsv = True
        # else:
        #     gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        #     hsv = False

    ## display the result
    try:
        cv.imshow('frame', gray)
    except:
        cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q') or cv.getWindowProperty("frame", cv.WND_PROP_VISIBLE) <1:
        break

# release the capture and destroy windows
cam.release();
cv.destroyAllWindows()
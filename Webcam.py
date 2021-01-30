import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, img = cam.read()
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grey1 = cv2.cvtColor(grey,cv2.COLOR_GRAY2BGR)
    print(grey1.shape)
    print(img.shape)
    blur = cv2.GaussianBlur(grey, (7,7), 0)
    canny = cv2.Canny(blur, 50, 50)
    canny1 = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    print(canny1.shape)
    dilate = cv2.dilate(canny, None , iterations=1)
    erode = cv2.erode(dilate, None, iterations=1)
    img1 = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    img2 = cv2.resize(grey1, (0, 0), None, 0.5, 0.5)
    img3 = cv2.resize(canny1, (0, 0), None, 0.5, 0.5)
    ver = np.vstack((img1,img3))
    hor = np.hstack((img1, img2, ver))
    cv2.imshow('Webcam', hor)
#    cv2.imshow('Webcam Gray', img2)
    if cv2.waitKey(10) == ord('q'):
        break

import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)

#img[:] = 0, 250, 150        # colours the image
cv2.line(img,(0,0),(img.shape[1], img.shape[0]), (0,250,0),2)
cv2.circle(img, (90,300), 80, (250,150,0), cv2.FILLED)
cv2.rectangle(img,(300,80),(500,200), (175,150,160), cv2.FILLED)
cv2.putText(img, 'OpenCv', (100,500), cv2.FONT_HERSHEY_DUPLEX, 3, (250,0,0), 2)
cv2.resize(img,)
cv2.imshow("Image", img)
cv2.waitKey(0)
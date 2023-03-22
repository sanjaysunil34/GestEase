import cv2 as cv
import numpy as np
import os
dirname = os.path.dirname(__file__)

cam = cv.VideoCapture(0)
count=0
while True:
    ret, img = cam.read()
    cv.imshow("Test", img)
    if not ret:
        break
    k=cv.waitKey(1)
    if k%256==27:
        print("Close")
        break
    elif k%256==32:
        print("Working")
        parent = os.path.dirname(dirname)
        main_dir = os.path.dirname(parent)
        file = os.path.join(main_dir, 'Electron/images/'+str(count)+'.jpg')
        print(file)
        # file = 'Electron/images/'+str(count)+'.jpg'
        cv.imwrite(file, img)
        count += 1
        print("Close")
        break
cam.release
cv.destroyAllWindows

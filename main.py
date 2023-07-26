import cv2 
from algCircle import CircleImg
from algRectangle import RectImg
import numpy as np
video = cv2.VideoCapture(0)

# recognize circles

while True:
    success, liveImg = video.read()
    # liveImg = cv2.imread(r".\Images\test\images\\15.jpg")

    if success:



        # circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
        circleImg = RectImg(liveImg)

        circleImg.thresholdByKernel((3, 3))
        circleImg.recognizeRectangle()
        circleImg.mark()
        cv2.waitKey(1500)
            



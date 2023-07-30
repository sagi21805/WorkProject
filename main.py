import cv2 
# from algCircle import CircleImg
from algRectangle import RectImg
import numpy as np
import psutil
video = cv2.VideoCapture(0)

# recognize circles

liveImg = cv2.imread("0003.jpg")

# if success:


print("started")
# circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
circleImg = RectImg(liveImg)

circleImg.imgPrep()
circleImg.recognizeRectangle()
cv2.namedWindow("marked")  
cv2.setMouseCallback("marked",circleImg.markByClicking)  


while True:
    # success, liveImg = video.read()
    cv2.imshow("marked", circleImg.markedImg)
    cv2.waitKey(1)
            



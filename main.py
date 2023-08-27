import cv2 
from algs.algRectangle import RectImg
import numpy as np
# video = cv2.VideoCapture(0)

# recognize circles

liveImg = cv2.imread("0004.jpg")

# if success:


print("started")
# circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
circleImg = RectImg(liveImg)
circleImg.mainRect(6, np.sum)
cv2.namedWindow("marked")  
cv2.setMouseCallback("marked",circleImg.markByClicking)  


while True:
    # success, liveImg = video.read()
    cv2.imshow("marked", circleImg.markedImg)
    cv2.imshow("p", circleImg.prepedImg)
    cv2.waitKey(1)
# cv2.imshow("r", circleImg.markedImg)
# cv2.waitKey(0)
            



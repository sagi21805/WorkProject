import cv2 
from algRectangle import RectImg
import numpy as np
<<<<<<< HEAD
import multiprocessing
from algCircle import CircleImg

if __name__ == "__main__":
    multiprocessing.freeze_support()
    video = cv2.VideoCapture(0)
    while True:    
        success, liveImg = video.read()
        # recognize circles

        # liveImg = cv2.imread("0033.jpg")

        # if success:


        print("started")
        # circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
        circleImg = RectImg(liveImg)
        circleImg.mainRect(7, np.sum)
        # circleImg.mark()

        cv2.imshow("p", circleImg.prepedImg)
        cv2.waitKey(1)
    # cv2.imshow("r", circleImg.markedImg)
    # cv2.waitKey(0)
=======
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
>>>>>>> 97882c0b96102e89f57bbea3ccee5ed09476989c
            



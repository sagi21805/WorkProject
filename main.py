import cv2 
from algRectangle import RectImg
import numpy as np
import multiprocessing
# recognize circles


# circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
if __name__ == "__main__":
    # video = cv2.VideoCapture(0)
    # success, liveImg = video.read()
    liveImg = cv2.imread("0003.jpg")
    circleImg = RectImg(liveImg)

    multiprocessing.freeze_support()
    print("started")
    circleImg.mainRect(2, np.sum)
    # circleImg.markAll()
    # cv2.waitKey(0)
    cv2.namedWindow("marked")  
    cv2.setMouseCallback("marked",circleImg.markByClicking)  


    while True:
        cv2.imshow("marked", circleImg.markedImg)
        cv2.imshow("p", circleImg.prepedImg)
        cv2.waitKey(1)
# cv2.imshow("r", circleImg.markedImg)
# cv2.waitKey(0)
            



import cv2 
from algRectangle import RectImg
import numpy as np
import multiprocessing
from algCircle import CircleImg
from XRayTarget import XRayTarget

if __name__ == "__main__":
    multiprocessing.freeze_support()
    video = cv2.VideoCapture(0)
    success, liveImg = video.read()
    # recognize circles

    # liveImg = cv2.imread("00010.jpg")

    # if success:


    print("started")
    # circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
    circleImg = CircleImg(liveImg)
    circleImg.main(2, np.sum)
    # circleImg.mark()
    cv2.namedWindow("marked")  
    cv2.setMouseCallback("marked",circleImg.markByClicking)  

            # success, liveImg = video.read()
    while True:
        cv2.imshow("marked", circleImg.markedImg)
        cv2.imshow("p", circleImg.prepedImg)
        cv2.waitKey(1)
    # cv2.imshow("r", circleImg.markedImg)
    # cv2.waitKey(0)
            



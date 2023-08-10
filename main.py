import cv2 
from algs.algCircle import CircleImg
from algs.algRectangle import RectImg
import multiprocessing
import numpy as np

if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    while True:
        success, liveImg = video.read()
        # recognize circles

        # liveImg = cv2.imread("00010.jpg")

            # if success:


        print("started")
        # circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
        circleImg = CircleImg(liveImg)
        circleImg.main(2)
        circleImg.mark()
        # cv2.namedWindow("marked")  
        # cv2.setMouseCallback("marked",circleImg.markByClicking)  

                # success, liveImg = video.read()
        cv2.imshow("marked", circleImg.markedImg)
        cv2.waitKey(1)
            # cv2.imshow("r", circleImg.markedImg)
            # cv2.waitKey(0)
            



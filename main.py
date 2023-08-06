import cv2 
from algRectangle import RectImg
import numpy as np
import multiprocessing
import time

if __name__ == "__main__":
    st = time.time()
    multiprocessing.freeze_support()

    liveImg = cv2.imread("0004.jpg")



    print("started")
    circleImg = RectImg(liveImg)
    circleImg.mainRect(6, np.sum)
    cv2.namedWindow("marked")  
    cv2.setMouseCallback("marked",circleImg.markByClicking)  
    ed = time.time()

    print(f"time: {ed - st}")

    while True:
        cv2.imshow("p", circleImg.prepedImg)
        cv2.imshow("r", circleImg.markedImg)
        cv2.waitKey(1)
                



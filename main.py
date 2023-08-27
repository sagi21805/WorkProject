import cv2 
from algs.algCircle import CircleImg
from algs.algRectangle import RectImg
import multiprocessing
import numpy as np

if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    # while True:
        # success, liveImg = video.read()
    # recognize circles

    liveImg = cv2.imread("./Images/0003.jpg")

    # if success:


    print("started")
    # circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
    circleImg = RectImg(liveImg)
    circleImg.main(2, np.sum)
    circleImg.mark()

        # success, liveImg = video.read()
    cv2.imshow("marked", circleImg.markedImg)
    cv2.imshow("p", circleImg.prepedImg)
    cv2.waitKey(0)
    # cv2.imshow("r", circleImg.markedImg)
    # cv2.waitKey(0)
            



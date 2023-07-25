import cv2
import numpy as np
from abc import ABC


class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = liveImg
        self.shapesContours = []
        self.shapesConstants = {}
        self.pixelsToMicroMeter = 1.74
        self.lenSize = 10

    def imgPrep(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        # adjusted = cv2.convertScaleAbs(gray, alpha=4, beta=-300) #alpha = contrast, beta = brightness
        lower_thresh = 255/5
        upper_thresh = 255

        ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        thresh = cv2.bilateralFilter(thresh, 15, 150, 150)

        sharpen = np.array([[ 0, -1,  0],
                            [-1,  5, -1], 
                            [ 0, -1,  0]])


        dst = cv2.filter2D(thresh, -1, sharpen)
        cv2.imshow("dst1",dst)

        bliateral = cv2.bilateralFilter(dst, 15, 200, 200)


        canny = cv2.Canny(dst , lower_thresh ,upper_thresh)
        cv2.imshow("gray", gray)
        cv2.imshow("bliateral", bliateral)
        cv2.imshow("dst2",dst)
        cv2.imshow("thresh",thresh)
        canny = cv2.dilate(canny, np.ones((2, 2), np.uint8), iterations=1)

        cv2.imshow("canny", canny)


        self.prepedImg = canny

    def clear(self):
        self.shapesContour = []
        self.shapesConstants = {}


    

    
        
    
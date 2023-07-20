import cv2
import numpy as np

class Img:

    def __init__(self, liveImg) -> None:
        self.img = cv2.resize(liveImg, (1269, 714))
        self.shape: tuple[int, int, int] = self.img.shape
        self.shapesContours = []
        self.shapesConstants = {}
        self.pixelsToMicroMeter = 1.74
        self.lenSize = 10

    def imgPrep(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        bliateral = cv2.bilateralFilter(gray, 10, 45, 45)
        lower_thresh = 255/5
        upper_thresh = 255
        canny = cv2.Canny(bliateral , lower_thresh ,upper_thresh)
        self.perpedImg = cv2.dilate(canny, np.ones((1, 1), np.uint8))

    def clear(self):
        self.shapesContour = []
        self.shapesConstants = {}




    

    
        
    
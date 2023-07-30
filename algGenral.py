import cv2
import numpy as np
from abc import ABC
from skimage.measure import block_reduce
class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.shapesContours = []
        self.shapesConstants = {}
        self.lenSize = 10
        self.pixelToMicro = 0.174 * self.lenSize

    @staticmethod
    def thresholdByKernel(img, kernelSize: tuple[int, int]):

        cv2.imshow("shrap", cv2.resize(img, (1280, 720)))
        x = block_reduce(img, kernelSize, np.sum, 1)
        threshold = (np.average(x) * 0.666 + 127.5)
        output = np.zeros(x.shape, np.uint8)
        for r, row in enumerate(x):
            for p ,pixel in enumerate(row):
                if pixel > threshold:
                    output[r][p] = 255
        
        return output
  
        
    def imgPrep(self):
        
        filter = np.array([[-1, -1,  -1], 
                           [-1,  10, -1], 
                           [-1, -1,  -1]])
        
        sharpend = cv2.filter2D(self.gray, -1, filter)
        self.prepedImg = Img.thresholdByKernel(sharpend, (3, 3))
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0] ))

        



    
        
    
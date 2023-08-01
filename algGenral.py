import cv2
import numpy as np
from abc import ABC
import numpy.lib.stride_tricks
class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.shapesContours = []
        self.shapesConstants = {}
        self.lenSize = 10
        self.pixelToMicro = 0.174 * self.lenSize
  
    def imgPrep(self, s, func):
        
        resized = cv2.resize(self.gray, np.flip(np.array(self.gray.shape)//3))  
        filter = np.array([[-1, -1,  -1], 
                           [-1,  10, -1], 
                           [-1, -1,  -1]])
        
        sharpend = cv2.filter2D(resized, -1, filter)
        sharpend = cv2.bilateralFilter(sharpend, 15, 75, 75)
        self.prepedImg = Img.applyWindow(sharpend, s, func)
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0]))
    
    @staticmethod
    def applyWindow(arr1, s, func):
        blocked = numpy.lib.stride_tricks.sliding_window_view(arr1, (s, s))
        x = func(blocked, axis = tuple(range(arr1.ndim, blocked.ndim)))
        thresh = np.average(x)*0.7
        x[x < thresh] = 0
        x[x > thresh] = 255
        print("finished")
        return np.array(x, dtype=np.uint8)

        



    
        
    
import cv2
import numpy as np
from abc import ABC
import numpy.lib.stride_tricks
class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.lenSize = 5
        self.pixelToMicro = -0.348 * self.lenSize + 5.22
  
    def imgPrep(self, s, func):
        #TODO try avarage and than canny on window
        resized = cv2.resize(self.gray, np.flip(np.array(self.gray.shape)//3))  
        # filter = np.array([[-1, -1,  -1], 
        #                    [-1,  10, -1], 
        #                    [-1, -1,  -1]])
        
        # sharpend = cv2.filter2D(resized, -1, filter)
        blured = cv2.bilateralFilter(resized, 15, 75, 75)
        self.prepedImg = Img.applyWindow(blured, s, func)
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0]))
    
    @staticmethod
    def applyWindow(arr1, s, func):
        blocked = numpy.lib.stride_tricks.sliding_window_view(arr1, (s, s))
        x = func(blocked, axis = tuple(range(arr1.ndim, blocked.ndim)))
        print(np.average(x)*0.5)
        thresh = np.average(x)*0.5
        x[x < thresh] = 0
        x[x > thresh] = 255
        print("finished")
        return np.array(x, dtype=np.uint8)
    
    #TODO work on the threshold
    #TODO make it work on circles
    #TODO add live window next to the img
    #TODO imporve software


        



    
        
    
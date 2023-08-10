import cv2
import numpy as np
from abc import ABC
import numpy.lib.stride_tricks
from numba import jit

class Img(ABC):

    def __init__(self, liveImg: np.ndarray) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.lenSize = 5
        self.pixelToMicro = 0.174 * self.lenSize
  
    def imgPrep(self, s):
        #TODO try avarage and than canny on window
        resized = cv2.resize(self.gray,  (1280, 720))  
        # filter = np.array([[-1, -1,  -1], 
        #                    [-1,  10, -1], 
        #                    [-1, -1,  -1]])
        
        # sharpend = cv2.filter2D(resized, -1, filter)
        blured = cv2.bilateralFilter(resized, 15, 75, 75)
        self.prepedImg = applyWindow(blured, s)
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0]))
    
@jit(nopython=True)
def applyWindow(img: np.ndarray, s):
    thresh = 255*s*s*0.3
    blocked = numpy.lib.stride_tricks.sliding_window_view(img, (s, s))
    new = np.zeros((blocked.shape[0], blocked.shape[1]), dtype=np.uint8)
    for i, row in enumerate(blocked):
        for j, block in enumerate(row):
            if np.sum(block) > thresh:
                new[i][j] = 255
    return new
    #TODO work on the threshold
    #TODO make it work on circles
    #TODO add live window next to the img
    #TODO imporve software


        



    
        
    
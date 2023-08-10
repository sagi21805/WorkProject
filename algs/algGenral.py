import cv2
import numpy as np
from abc import ABC
import numpy.lib.stride_tricks
from numba import njit, prange

class Img(ABC):

    def __init__(self, liveImg: np.ndarray) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.lenSize = 10
        self.pixelToMicro = 0.174 * self.lenSize
  
    def imgPrep(self, s):
        #TODO try avarage and than canny on window
        resized = cv2.resize(self.gray,  (1280, 720))  
        # filter = np.array([[-1, -1,  -1], 
        #                    [-1,  10, -1], 
        #                    [-1, -1,  -1]])
        
        # sharpend = cv2.filter2D(resized, -1, filter)
        blured = cv2.bilateralFilter(resized, 20, 75, 75)
        self.prepedImg = applyWindow(blured, s)
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0]))
    
@njit(fastmath=True)
def applyWindow(img: np.ndarray, s):
    thresh = 255*s*s*0.15
    blocked = numpy.lib.stride_tricks.sliding_window_view(img, (s, s))
    new = np.zeros((blocked.shape[0], blocked.shape[1]), np.uint8)
    for i in prange(len(blocked)):
        for j in prange(len(blocked[0])):
            if np.sum(blocked[i][j]) > thresh:
                new[i][j] = 255
    return new
    #TODO work on the threshold
    #TODO make it work on circles
    #TODO add live window next to the img
    #TODO imporve software


        



    
        
    
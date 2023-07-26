import cv2
import numpy as np
from abc import ABC
import skimage.measure

class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.shapesContours = []
        self.shapesConstants = {}
        self.lenSize = 10
        self.pixelToMicro = 0.174 * self.lenSize

    def thresholdByKernel(self, kernelSize: tuple[int, int]):
        x = skimage.measure.block_reduce(self.gray, kernelSize, np.sum, 1)
        threshold = (np.average(x) * 0.666 + 127.5)
        self.prepedImg = np.zeros(x.shape, np.uint8)
        for r, row in enumerate(x):
            for p ,pixel in enumerate(row):
                if pixel > threshold:
                    self.prepedImg[r][p] = 255

    def clear(self):
        self.shapesContour = []
        self.shapesConstants = {}


    

    
        
    
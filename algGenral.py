import cv2
import numpy as np
from abc import ABC


class Img(ABC):

    def __init__(self, liveImg) -> None:
        self.img = cv2.resize(liveImg, (int(liveImg.shape[1]*40/100), int(liveImg.shape[0]*40/100)))
        self.img = liveImg
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
        self.perpedImg = cv2.dilate(canny, np.ones((1, 1), np.uint8), iterations=2)

    def clear(self):
        self.shapesContour = []
        self.shapesConstants = {}

    def ApplyFillter(self, kernelSize: tuple[int, int], fillter: list[list], stride: int  = 1):
        self.imgAfterFillter = []
        fillterMatrix = np.array(fillter)
        pixelTimes = 0
        rowTimes = 0
        data = np.array(self.img)
        data = data.reshape(self.img.shape[0], self.img.shape[1])  
        for n in range(int(np.ceil((self.img.shape[1] - kernelSize[1]) / stride))):     
            for i in range(int(np.ceil((self.img.shape[0] - kernelSize[0]) / stride))):
                kernel = []    
                for row in range(stride * rowTimes, (kernelSize[1] + (stride * rowTimes))):
                    pixelList = []
                    for pixel in range(stride * pixelTimes, (kernelSize[0] + (stride * pixelTimes))):
                        pixel = data[row][pixel]
                        pixelList.append(pixel)
                    kernel.append(pixelList)
                kernel = np.array(kernel)
                newPixel = kernel * fillterMatrix
                self.imgAfterFillter.append(newPixel.sum())
                pixelTimes += 1
            rowTimes += 1
            pixelTimes = 0
        self.imgAfterFillter = np.array(self.imgAfterFillter)



    

    
        
    
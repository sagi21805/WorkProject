import math
import cv2
import numpy as np
from algGenral import Img

class RectImg(Img):
    
    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)
        self.aprrovedRect = []
        self.rectList = []

    def recognizeRectangle(self):
        cv2.imshow("img", self.prepedImg)
        rectContours, hierarchy = cv2.findContours(self.prepedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        hierarchy = hierarchy[0]
        if len(rectContours) != 0:
            #[next, previous, first child, parent] --> hierarchy 
            for index, contour in enumerate(rectContours):
                if hierarchy[index][2] != -1 and hierarchy[index][3] != -1:
                    # if hierarchy[hierarchy[index][2]][2] == -1:
                        # if cv2.contourArea(contour) > 100:
                        rect = cv2.minAreaRect(contour)
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        self.rectList.append(box)
                        # print("contour ->")
                        # print(contour)
                        # print("rect ->")
                        # print(rect)
                        # print("box - >")
                        # print(box)
                        self.shapesConstants.update({"rectList" : self.rectList})
                        self.shapesContours.append(rectContours)

    
    def  mark(self):
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0] ))
        pixelToMicro = self.img.shape[1] / self.markedImg.shape[1] * self.pixelToMicro 
        for i, rect in enumerate(self.rectList):
            if np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1])  , 2) < 150 and np.round(np.sqrt((rect[1][0] - rect[2][0])**2 + (rect[1][1] - rect[2][1])**2) * self.pixelToMicro , 2) > 300:
                cv2.drawContours(self.markedImg,[rect],0,(0,255,255),1)
                cv2.putText(self.markedImg, str(np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) * self.pixelToMicro , 2)), rect[i % 2 + 1], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.imshow("nar", self.markedImg)

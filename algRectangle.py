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
        self.imgPrep()
        cv2.imshow("img", self.prepedImg)
        self.rectContours, _ = cv2.findContours(self.prepedImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if len(self.rectContours) != 0:
            for contour in self.rectContours:
                if cv2.contourArea(contour) > 100:
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
                    self.shapesContours.append(self.rectContours)

    def stayblize(self):
        # bad way improve
        self.aprrovedRect = self.rectList
        for i, rect in enumerate(self.rectList):
            # if np.sqrt((rect[0][0] - rect[3][0])**2 + (rect[0][1] - rect[3][1])**2) < 450:
            #     self.aprrovedRect.pop(i)
            #     continue
            for rect2 in self.rectList:                    
                    dist = np.sqrt((rect[0][0] - rect2[0][0])**2 + (rect[0][1] - rect2[0][1])**2)
                    if dist < 100 and dist != 0:
                        if cv2.contourArea(rect) > cv2.contourArea(rect2):
                            self.aprrovedRect.pop(i)
                            
    def mark(self):
        self.markedImg = self.img
        for rect in self.rectList:
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),2)
            cv2.putText(self.markedImg, str(np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2), 2)), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("nar", self.markedImg)

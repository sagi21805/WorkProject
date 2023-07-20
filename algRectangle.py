import cv2
import numpy as np
from algGenral import Img

class RectImg(Img):
    
    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)
        self.aprrovedRect = {}
        self.rectList = []

    def recognizeRectangle(self):
        self.imgPrep()
        cv2.imshow("img", self.perpedImg)
        self.rectContours, _ = cv2.findContours(self.perpedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(self.rectContours) != 0:
            for contour in self.rectContours:
                if cv2.contourArea(contour) > 310.5:
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
        pass

    def mark(self):
        for rect in self.rectList:
            self.markedImg = cv2.drawContours(self.img ,[rect],0,(0,255,255),2)
            self.markedImg = cv2.putText(self.markedImg, str(np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2), 2)), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)



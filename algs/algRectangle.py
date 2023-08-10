import cv2
import numpy as np
from algGenral import Img
import multiprocessing.pool
import time

class RectImg(Img):
    
    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)
        self.aprrovedRect = []
        self.rectList = []

    def main(self, s):
        st = time.time()
        self.rec(s)
        print(f"time: {time.time() - st}")
        cv2.imshow("p", self.prepedImg)


    def rec(self, s):
        self.imgPrep(s)
        self.rectContours, hierarchy = cv2.findContours(self.prepedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(self.rectContours) != 0:
            #[next, previous, first child, parent] --> hierarchy 
            hierarchy = hierarchy[0]

            for contour in self.rectContours:
                # if hierarchy[index][2] == -1:
                if cv2.contourArea(contour) > 200:
                    rect = cv2.minAreaRect(contour)
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    self.rectList.append(box)
    
                


        return [self.prepedImg, self.markedImg, self.rectList, self.rectContours]

    
    def mark(self):
        for rect in self.rectList:
            cv2.putText(self.markedImg, str(np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            # if np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1])  , 2) < 150 and np.round(np.sqrt((rect[1][0] - rect[2][0])**2 + (rect[1][1] - rect[2][1])**2) * self.pixelToMicro , 2) > 300:
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),1)
            cv2.imshow("markedImage", self.markedImg)
    
                
    def markAll(self):
        for rect in self.rectContours:
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),2)
        cv2.imshow("nar", self.markedImg)
            
    # TODO improve with numpy!
    
    def findClosestPoint(self, x, y):
        closetPointDist = np.inf
        closetBox = []
        for box in self.rectList: 
            for point in box:
                if np.sqrt((point[0] - x)**2 + (point[1] - y)**2) < closetPointDist:
                    closetPointDist = np.sqrt((point[0] - x)**2 + (point[1] - y)**2)
                    closetBox = box
        return closetBox
    
    def markByClicking(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            rect = self.findClosestPoint(x, y)
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),1)
            cv2.putText(self.markedImg, str(np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 10), 2, cv2.LINE_AA)
        
                

import cv2
import numpy as np
import multiprocessing.pool
import random as r
from numba import jit
from algGenral import Img

 # dict of types {float : tuple} 
class CircleImg(Img):

    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)
        self.circles = {}

    def main(self, s, func):
        with multiprocessing.pool.Pool(8) as p:
            r = p.starmap(self.recognizeRectangle, [(s, func), ])
        self.prepedImg = r[0][0]
        self.markedImg = r[0][1]
        self.circles = r[0][2]
        self.CircContours = r[0][3]
        cv2.imshow("p", self.prepedImg)

    def recognizeRectangle(self, s, func):
        self.imgPrep(s, func)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
        self.prepedImg = cv2.morphologyEx(self.prepedImg, cv2.MORPH_ELLIPSE, kernel, iterations=1)

        CircContours, hierarchy = cv2.findContours(self.prepedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(CircContours) != 0:
            #[next, previous, first child, parent] --> hierarchy 
            hierarchy = hierarchy[0]

            for index, contour in enumerate(CircContours):
                    if cv2.contourArea(contour) > 200:
                        (x, y), r = cv2.minEnclosingCircle(contour)
                        self.circles.update({r : (round(x), round(y))})
            return [self.prepedImg, self.markedImg, self.circles, CircContours]            

    
    def mark(self):   
        for rad in self.circles:
            cv2.circle(self.markedImg, (self.circles[rad][0],self.circles[rad][1]), round(rad), (255, 0, 255), 2)
            cv2.putText(self.markedImg, str(np.round(2*rad/ self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)), ((self.circles[rad][0] - round(rad) ),self.circles[rad][1]) ,cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 0, 255), 2, cv2.LINE_AA)


    def findClosestPoint(self, x, y):
            closetPointDist = np.inf
            r = 0
            for rad in self.circles: 
                point = self.circles[rad]
                dist = np.sqrt((point[0] - x)**2 + (point[1] - y)**2)
                if dist < closetPointDist:
                    closetPointDist = dist
                    r = rad
            return r
        
    def markByClicking(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            rad = self.findClosestPoint(x, y)
            cv2.circle(self.markedImg, self.circles[rad], round(rad),(0, 255, 255),1)
            cv2.putText(self.markedImg, str(np.round(2*rad/ self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)),(x, y) ,cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 5, 255), 2, cv2.LINE_AA)
            del self.circles[rad]

    def markAll(self):
        for rad in self.circles:
            cv2.circle(self.markedImg,self.circles[rad], round(rad) ,(0,255,255),2)
            cv2.imshow("nar", self.markedImg)
            # img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), (round(x), round(y)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # img = cv2.putText(img, str((circle.x, circle.y, circle.r)), (round(x + 10), round(y + 10)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            





        




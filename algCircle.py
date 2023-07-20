import cv2
from algGenral import Img 
import numpy as np

 # dict of types {float : tuple} 
class CircleImg(Img):

    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)
        self.circleDict = {}
        self.aprrovedCircles = {}


    # worth trying with real camera and data
    def recognizeCircle(self):
        self.imgPrep()
        self.circleContour, _ = cv2.findContours(self.perpedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow("ca", self.perpedImg)
        if len(self.circleContour) != 0:
            for contour in self.circleContour:
                if cv2.contourArea(contour) > 55:
                    # (x, y), r = cv2.minEnclosingCircle(contour)
                    #find the center and the radius
                    M = cv2.moments(contour)
                    x = int(M["m10"] / M["m00"])
                    y = int(M["m01"] / M["m00"])
                    r = (np.sqrt(cv2.contourArea(contour) / np.pi) + cv2.arcLength(contour, True) / 2 /np.pi) / 2
                    self.circleDict.update({r : (round(x), round(y))})
                  
            self.shapesConstants.update({"circleDict" : self.circleDict})
            self.shapesContours.append(self.circleContour)

    def stayblize(self):
        arr = np.asarray([rad for rad in self.circleDict])
        for contour in self.circleContour:
            cntArea = cv2.contourArea(contour)
            if cntArea > 55:
                cntAproxRad = np.sqrt(cntArea/np.pi)
                i = (np.abs(arr - cntAproxRad)).argmin()
                self.aprrovedCircles.update({arr[i] : self.circleDict[arr[i]]})        
                # M = cv2.moments(c)
                # cX = int(M["m10"] / M["m00"])
                # cY = int(M["m01"] / M["m00"])
                                    
                

    def mark(self):
        for rad in self.aprrovedCircles:
            self.markedImg = cv2.circle(self.img, (self.aprrovedCircles[rad][0],self.aprrovedCircles[rad][1]), round(rad), (255, 0, 0), 2)
    
    def markUnstaybled(self):
        for rad in self.circleDict:
            self.markedImg = cv2.circle(self.img, (self.circleDict[rad][0],self.circleDict[rad][1]), round(rad), (255, 0, 255), 2)

    
    


            # img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), (round(x), round(y)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # img = cv2.putText(img, str((circle.x, circle.y, circle.r)), (round(x + 10), round(y + 10)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            





        




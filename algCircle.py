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
    def recognizeCircle(self, s, func):
        self.imgPrep(s, func)
        rectContours, hierarchy = cv2.findContours(self.prepedImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        hierarchy = hierarchy[0]
        if len(rectContours) != 0:
            #[next, previous, first child, parent] --> hierarchy 
            for index, contour in enumerate(rectContours):
                # if hierarchy[index][2] == -1:
                        if cv2.contourArea(contour) > 80:
                            rect = cv2.minAreaRect(contour)
                            box = cv2.boxPoints(rect)
                            box = np.int0(box)
                            self.rectList.append(box)

                                                

    def mark(self):
        for rad in self.aprrovedCircles:
            self.markedImg = cv2.circle(self.img, (self.aprrovedCircles[rad][0],self.aprrovedCircles[rad][1]), round(rad), (255, 0, 0), 2)
    
    def markUnstaybled(self):   
        for rad in self.circleDict:
            self.markedImg = cv2.circle(self.img, (self.circleDict[rad][0],self.circleDict[rad][1]), round(rad), (255, 0, 255), 2)

   
    


            # img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), (round(x), round(y)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            # img = cv2.putText(img, str((circle.x, circle.y, circle.r)), (round(x + 10), round(y + 10)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            





        




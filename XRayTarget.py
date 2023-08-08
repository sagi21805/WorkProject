import cv2
import numpy as np
from algGenral import Img
from algRectangle import RectImg

class XRayTarget(RectImg):

    def __init__(self, liveImg) -> None:
        super().__init__(liveImg)

        

    def markByClicking(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONUP:
            rect = self.findClosestPoint(x, y)
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),1)
            width = np.round(np.sqrt((rect[1][0] - rect[2][0])**2 + (rect[1][1] - rect[2][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)
            height = np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)
            cv2.putText(self.markedImg, str(height), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 0.69, (50, 255, 50), 1, cv2.LINE_AA)
            cv2.putText(self.markedImg, str(width), rect[1], cv2.FONT_HERSHEY_SIMPLEX, 0.69, (50, 50, 255), 1, cv2.LINE_AA)
            cv2.circle(self.markedImg, rect[0], 2, (0, 0, 255), 2)
            cv2.circle(self.markedImg, rect[1], 2, (0, 255, 0), 2)
            cv2.circle(self.markedImg, rect[2], 2, (255, 0, 0), 2)


    def mark(self):
        for rect in self.rectList:
            width = np.round(np.sqrt((rect[1][0] - rect[2][0])**2 + (rect[1][1] - rect[2][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)
            height = np.round(np.sqrt((rect[1][0] - rect[0][0])**2 + (rect[1][1] - rect[0][1])**2) / self.pixelToMicro * (self.img.shape[1] / self.markedImg.shape[1]), 2)
            # if width * height > 4225:
            cv2.drawContours(self.markedImg,[rect],0,(0,255,255),1)
            cv2.putText(self.markedImg, str(height), rect[0], cv2.FONT_HERSHEY_SIMPLEX, 0.69, (50, 255, 50), 2, cv2.LINE_AA)
            cv2.putText(self.markedImg, str(width), rect[1], cv2.FONT_HERSHEY_SIMPLEX, 0.69, (50, 50, 255), 2, cv2.LINE_AA)
            cv2.circle(self.markedImg, rect[0], 2, (0, 0, 255), 2)
            cv2.circle(self.markedImg, rect[1], 2, (0, 255, 0), 2)
            cv2.circle(self.markedImg, rect[2], 2, (255, 0, 0), 2)







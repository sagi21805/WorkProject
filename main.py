import cv2 
from algCircle import CircleImg
from algRectangle import RectImg
import numpy as np
video = cv2.VideoCapture(0)

# recognize circles

# while True:
# success, liveImg = video.read()
liveImg = cv2.imread(r"C:\VsCode\python\WorkProject\Images\test\images\\6.jpg")

# if success:

circleImg = RectImg(cv2.resize(liveImg, (1536, 864)))
circleImg.recognizeRectangle()
circleImg.mark()
print(2)
# filter = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# fillter = cv2.filter2D(circleImg.img, -1, filter)
cv2.waitKey(0)
        



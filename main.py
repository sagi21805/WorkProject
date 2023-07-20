import cv2 
from algCircle import CircleImg
from algGenral import Img
video = cv2.VideoCapture(0)

# recognize circles

while True:
    success, liveImg = video.read()
    if success:
        circleImg = CircleImg(liveImg)

        circleImg.recognizeCircle()
        circleImg.stayblize()
        circleImg.mark()
        try:
            cv2.imshow("marked img", circleImg.markedImg)
        except:
            pass
        circleImg.markUnstay()
        try:
            cv2.imshow("unmarked img", circleImg.markedImg)
        except:
            pass
        cv2.waitKey(1)



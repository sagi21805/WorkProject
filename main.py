import cv2 
from algCircle import CircleImg
from algRectangle import RectImg
video = cv2.VideoCapture(0)

# recognize circles

while True:
    success, liveImg = video.read()
    # liveImg = cv2.imread("rectangle_small.jpg")
    if success:

        try:    
            circleImg = RectImg(cv2.resize(liveImg, (int(liveImg.shape[1]*40/100), int(liveImg.shape[0]*40/100))))
            circleImg.recognizeRectangle()
            circleImg.stayblize()
            circleImg.mark()

            cv2.imshow("marked img", circleImg.markedImg)
        except:
            pass
    cv2.waitKey(1)
        



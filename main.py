import cv2 
from algCircle import CircleImg
from algRectangle import RectImg
video = cv2.VideoCapture(0)

# recognize circles

while True:
    # success, liveImg = video.read()
    liveImg = cv2.imread("rectangle_small.jpg")
    # if success:
    circleImg = RectImg(liveImg)
    circleImg.recognizeRectangle()
    circleImg.stayblize()
    circleImg.mark()

    try:
        cv2.imshow("marked img", circleImg.markedImg)
    except:
        pass
    cv2.waitKey(0)
        



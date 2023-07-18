import algorithems
import cv2 

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    if success:
        cv2.imshow("img", algorithems.recognizeCircle(algorithems.recognizeRectangle(img)))
        


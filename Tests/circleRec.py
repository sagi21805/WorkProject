import cv2
import numpy as np


video = cv2.VideoCapture(0)
PIXELS_TO_MICROMETER = 1.74

while True:
    success, img = video.read()
    if success:
        img = cv2.resize(img, (1269, 714))
        ret,thresh = cv2.threshold(img,127,255,0)
        canny = cv2.Canny(thresh, 200 ,1529)
        contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.waitKey(1)
        for contour in contours:
            if cv2.contourArea(contour) > 15:
                # rect = cv2.minAreaRect(contour)
                # box = cv2.boxPoints(rect)
                # box = np.int0(box)
                # img = cv2.drawContours(img,[box],0,(0,255,255),2)
                (x, y), r = cv2.minEnclosingCircle(contour)
                center = (round(x), round(y))
                # x, y, w, h = cv2.boundingRect(contour)  
                font = cv2.FONT_HERSHEY_SIMPLEX          
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
                cv2.circle(img, center, round(r), color, 2)
                img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), center , font, fontScale, (0, 0, 255), thickness, cv2.LINE_AA)
# np.round(np.sqrt((box[1][0] - box[0][0])**2 + (box[1][1] - box[0][1])**2) * PIXELS_TO_MICROMETER
                cv2.imshow("one", img)
                # # cv2.imshow("one2", blur)
                # cv2.imshow("one3", mask)
                cv2.imshow("c2", canny)
cv2.contou
                
                


# cv2.imshow("one4", erode)
# cv2.imshow("d", dilate)

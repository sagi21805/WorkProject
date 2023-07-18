import cv2
import numpy as np


PIXELS_TO_MICROMETER = 1.74

def recognizeCircle(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _ ,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    canny = cv2.Canny(thresh, 200 ,1529)
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.waitKey(1)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 15:
                (x, y), r = cv2.minEnclosingCircle(contour)
                cv2.circle(img, (round(x), round(y)), round(r), (255, 0, 0), 2)
                img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), (round(x), round(y)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                #TODO - try with circle area
    return img

def recognizeRectangle(img):
    mask = cv2.inRange(img, (0, 0, 0), (120, 120, 120))
    canny = cv2.Canny(mask, 200 ,1529)
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 200:
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                img = cv2.drawContours(img,[box],0,(0,255,255),2)
                img = cv2.putText(img, str(np.round(np.sqrt((box[1][0] - box[0][0])**2 + (box[1][1] - box[0][1])**2) * PIXELS_TO_MICROMETER, 2)), box[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img

def stabilizer():
    #TODO - camera needed
    pass



        




import cv2
import numpy as np

def recognizeRectangle(canny, img):
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 50:
                rect = cv2.minAreaRect(contour)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                img = cv2.drawContours(img,[box],0,(0,255,255),2)
                img = cv2.putText(img, str(np.round(np.sqrt((box[1][0] - box[0][0])**2 + (box[1][1] - box[0][1])**2) * PIXELS_TO_MICROMETER, 2)), box[0], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img
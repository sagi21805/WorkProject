import cv2
import numpy as np

img = cv2.imread("rectangle.jpg")
mask = cv2.inRange(img, (0, 0, 0), (120, 120, 120))
canny = cv2.Canny(mask, 200 ,1529)
PIXELS_TO_MICROMETER = 1
contours, hierarchies = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
if len(contours) != 0:
    for contour in contours:
        if cv2.contourArea(contour) > 200:
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            img = cv2.drawContours(img,[box],0,(0,255,255),2)
            font = cv2.FONT_HERSHEY_SIMPLEX          
            org = box[0]
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            img = cv2.putText(img, str(np.round(np.sqrt((box[1][0] - box[0][0])**2 + (box[1][1] - box[0][1])**2) * PIXELS_TO_MICROMETER, 2)), org, font, fontScale, color, thickness, cv2.LINE_AA)
            


cv2.imshow("one", img)
# cv2.imshow("one2", blur)
cv2.imshow("one3", mask)
cv2.imshow("c2", canny)

# cv2.imshow("one4", erode)
# cv2.imshow("d", dilate)



cv2.waitKey(0)
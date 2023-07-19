import cv2
import math

PIXELS_TO_MICROMETER = 1.74
circleDict = {} # dict of types {float : tuple} 


@staticmethod
def stabilizerCircle(circlesDetectedRadius: list[float]):
    circlesDetectedRadius.sort()
    allSimilars = []
    for rad1 in circlesDetectedRadius:
        similar = [rad1]
        for rad2 in circlesDetectedRadius:
            if rad1 / rad2 > 0.9 and rad1 / rad2 < 1:
                if math.dist(circleDict[rad1],  circleDict[rad2]) < 100:
                    similar.append(rad2)
        similar.remove(max(similar))
        allSimilars.append(similar)
    for similarL in allSimilars:
        for key in similarL:
            try:
                del circleDict[key]
            except: 
                pass

    #TODO - IMPROVE THE SIMILARITIES DETECTION

            
                
    
@staticmethod
def recognizeCircle(canny, img):
    circlesDetectedRadius: list[float] = []
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("ca", canny)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 55:
                (x, y), r = cv2.minEnclosingCircle(contour)
                circleDict.update({r : (round(x), round(y))})
                # img = cv2.putText(img, str(round(int(r)* 2 * PIXELS_TO_MICROMETER, 2)), (round(x), round(y)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # img = cv2.putText(img, str((circle.x, circle.y, circle.r)), (round(x + 10), round(y + 10)) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                circlesDetectedRadius.append(r)
                
                #TODO - try with circle area
    return [img, circlesDetectedRadius]

@staticmethod
def markCircles(img):
    print(len(circleDict))
    for rad in circleDict:
        cv2.circle(img, (circleDict[rad][0],circleDict[rad][1]), round(rad), (255, 0, 0), 2)
    return img
        





        




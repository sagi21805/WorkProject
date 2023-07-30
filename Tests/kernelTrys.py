import cv2
import numpy as np


def imgPrep(img, kernel):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adjusted = cv2.convertScaleAbs(gray, alpha=4, beta=-300) #alpha = contrast, beta = brightness
    bliateral = cv2.bilateralFilter(adjusted, 10, 75, 75)
    lower_thresh = 255/5
    upper_thresh = 255
    dst = cv2.filter2D(gray, -1, kernel)
    bliateral = cv2.bilateralFilter(dst, 10, 75, 75)
    canny = cv2.Canny(bliateral , lower_thresh ,upper_thresh)
    cv2.imshow("gray", gray)
    cv2.imshow("bliateral", bliateral)
    cv2.imshow("adjh", adjusted)
    cv2.imshow("fillter",dst)
    return cv2.dilate(canny, np.ones((1, 1), np.uint8), iterations=2)


img = cv2.imread(r"C:\VsCode\python\WorkProject\rectangle_small.jpg")

edgeUp = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
edgeDown = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
edgeRight = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
edgeLeft = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

# edges are pretty similar

sharpen = np.array([[0, -1, 0],
                    [-1, 5, -1], 
                    [0, -1, 0]])

sharpenStrong = np.array([[ 0,  0, -1,  0, 0 ],
                            [ 0, -1, -2, -1, 0 ],
                            [-1, -2, 17, -2, -1], 
                            [ 0, -1, -2, -1,  0],
                            [ 0,  0, -1,  0,  0]])



fillters = [edgeUp, edgeDown, edgeRight, edgeLeft]


cv2.imshow("f",imgPrep(img, sharpen))



cv2.waitKey(0)

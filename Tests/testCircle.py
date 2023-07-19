import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("img")
while True:
    success, img = cap.read()
    ret,thresh = cv2.threshold(img,127,255,0)
    cv2.imshow("img2", img)
    cv2.imshow("img", thresh)
    cv2.waitKey(1)


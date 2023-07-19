import algCircle
import cv2 
import algGenral

video = cv2.VideoCapture(0)

success, img = video.read()
if success:
    canny = algGenral.imgPrep(img)
    img, circlesRad = algCircle.recognizeCircle(canny, cv2.resize(img, (1269, 714)))
    before = algCircle.markCircles(img)
    algCircle.stabilizerCircle(circlesRad)
    after = algCircle.markCircles(img)

    cv2.imshow("b", before)
    cv2.waitKey(0)



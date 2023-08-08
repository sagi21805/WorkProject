import scipy.signal
import cv2 
import numpy as np

filter = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
img = cv2.cvtColor(cv2.imread("./images/0004.jpg"), cv2.COLOR_BGR2GRAY)
img1 = cv2.cvtColor(cv2.imread("./images/0033.jpg"), cv2.COLOR_BGR2GRAY)
y = cv2.filter2D(img, -1, filter)
x = scipy.signal.fftconvolve(img, filter)
x = cv2.resize(x, (3840//3, 2160//3))
y = cv2.resize(y, (3840//3, 2160//3))
print(f"y: {y}")
print(f"x: {x}")
z = cv2.resize(img, (3840//3, 2160//3))

cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("Z", z)
cv2.waitKey(0)
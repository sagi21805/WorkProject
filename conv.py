import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time


arr1 = cv2.resize(cv2.cvtColor(cv2.imread("0007.jpg"), cv2.COLOR_BGR2GRAY), (640//3, 480//3))
arr2 = cv2.resize(cv2.cvtColor(cv2.imread("0005.jpg"), cv2.COLOR_BGR2GRAY), (640//3, 480//3))
arr3 = cv2.resize(cv2.cvtColor(cv2.imread("0003.jpg"), cv2.COLOR_BGR2GRAY), (640//3, 480//3))

cv2.imshow("1", arr1)
cv2.imshow("2", arr2)
cv2.imshow("3", arr3)

st = time.time()


a = scipy.signal.fftconvolve(arr3, arr2, "valid")


b = scipy.signal.fftconvolve(arr3, arr1, "valid")


c = scipy.signal.fftconvolve(arr3, arr3, "valid")
print(c)

print(f"time: {time.time() - st}")

plt.plot(np.sum(c, 0), color= "red") #monitor
plt.plot(np.sum(b, 0), color= "blue")
plt.plot(np.sum(a, 0), color="green")



plt.show()






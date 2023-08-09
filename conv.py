import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

arr1 = np.zeros((256, 256), np.uint8)
arr2 = np.zeros((256, 256), np.uint8)

cv2.rectangle(arr1, (25, 25), (100, 100), (255, 255, 255), -1)
cv2.rectangle(arr2, (100, 25), (175, 100), (255, 255, 255), -1)


cv2.imshow("1", arr1)
cv2.imshow("2", arr2)



a = scipy.signal.fftconvolve(arr1, arr2)


# b = scipy.signal.fftconvolve(arr1, arr1)





# plt.plot(np.sum(b, 0), color= "blue")
plt.plot(np.sum(a, 0), color="green")



plt.show()






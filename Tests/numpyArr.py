import numpy as np
from testThresholdByKernel import applyKernel
import cv2
from multiprocessing import Pool

arr1 = np.array([[1, 2, 3, 5, 5], 
                 [1, 5, 3, 5, 5], 
                 [1, 2, 3, 4, 5]])

arr2 = np.array([[1, 2, 3, 5], 
                 [1, 2, 9, 5], 
                 [1, 2, 9, 4],
                 [5, 6, 7, 8]])

arr3 = np.array([[2], [3]])

arr3[0][0] = 5
print(arr3)
# print(arr3)

a = arr1
a = a[:, 1:]
tup = (0, 0)
list = [5, 5]
tup = list
# print(tup)


img = cv2.imread("/home/sagi21805/Desktop/Vscode/python/WorkProject/0003.jpg", cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = applyKernel(img, 15, 1, 1, np.average)

with Pool(8) as pool:
    result = pool.map()


cv2.imshow("output", cv2.resize(x, (1280, 720)))
cv2.waitKey(0)
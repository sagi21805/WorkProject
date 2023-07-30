import numpy.lib.stride_tricks 
import numpy as np
import cv2
import time
import multiprocessing.pool

#change all lists into numpy arrays*** 


def working_window(arr1):
    s1 = 3
    s2 = 3
    blocked = numpy.lib.stride_tricks.sliding_window_view(arr1, (s1, s2))
    x = np.sum(blocked, axis = tuple(range(arr1.ndim, blocked.ndim)))
    thresh = 255*s1*s2*0.42
    x[x < thresh] = 0
    x[x > thresh] = 255
    print("finished")
    return np.array(x, dtype=np.uint8)
        
arr1 = cv2.imread("/home/sagi21805/Desktop/Vscode/python/WorkProject/0007.jpg")
arr1 = cv2.cvtColor(arr1, cv2.COLOR_BGR2GRAY)
arr1 = cv2.resize(arr1, np.flip(np.array(arr1.shape)//3))
arr1 = cv2.bilateralFilter(arr1, 15, 75, 75)
st = time.time()
with multiprocessing.pool.Pool(8) as p:
    r = p.map(working_window, (arr1, ))
ed = time.time()
print(f"time: {ed-st}")
cv2.imshow("r", r[0])
cv2.waitKey(0)







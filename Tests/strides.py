import numpy.lib.stride_tricks 
import numpy as np
import cv2
import time
import multiprocessing.pool

#change all lists into numpy arrays*** 
arr1 = np.array([[1, 2, 3, 5, 5], 
                 [1, 5, 3, 5, 5], 
                 [1, 2, 3, 4, 5]])

def working_window(arr1):
    
    s1 = 2
    s2 = 2
    blocked = numpy.lib.stride_tricks.sliding_window_view(arr1, (s1, s2))
    print("finished")
    print(blocked)
        

# arr1 = cv2.imread("/home/sagi21805/Desktop/Vscode/python/WorkProject/0007.jpg")
# arr1 = cv2.cvtColor(arr1, cv2.COLOR_BGR2GRAY)
# arr1 = cv2.resize(arr1, np.flip(np.array(arr1.shape)//3))
# arr1 = cv2.bilateralFilter(arr1, 15, 75, 75)
# st = time.time()
# p = multiprocessing.pool.Pool(12) 
# r = p.map(func=working_window, iterable=(arr1, ))
# p.close()    
# print(r)
    

working_window(arr1)







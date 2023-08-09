import time
from numba import njit
import numpy as np
import numpy.lib.stride_tricks
import cv2
import multiprocessing.pool
from cProfile import Profile
from pstats import SortKey, Stats

@njit(fastmath=True)
def func(img: np.ndarray, s):
    thresh = 255*s*s*0.3
    blocked = numpy.lib.stride_tricks.sliding_window_view(img, (s, s))
    new = np.zeros((blocked.shape[0], blocked.shape[1]))
    for i, row in enumerate(blocked):
        for j, block in enumerate(row):
            if np.sum(block) > thresh:
                new[i][j] = 255
    return new

def last():    
    v = cv2.VideoCapture(0)
    while True:
        suc, img = v.read()  
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (1280, 720))
        st = time.time()
        new = func(img, 3)
        print(time.time() - st)
        cv2.imshow("!", new)
        cv2.waitKey(1)
last()
    


    

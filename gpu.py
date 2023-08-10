import time
from numba import njit
from numba import prange
import numpy as np
import numpy.lib.stride_tricks
import cv2
from cProfile import Profile
from pstats import SortKey, Stats
import multiprocessing.pool


#for very large math like with s > 15 use with parallel=True

@njit(fastmath=True)
def func(img: np.ndarray, s):
    thresh = 255*s*s*0.3
    blocked = numpy.lib.stride_tricks.sliding_window_view(img, (s, s))
    new = np.zeros((blocked.shape[0], blocked.shape[1]), np.uint8)
    for i in prange(len(blocked)):
        for j in prange(len(blocked[0])):
            if np.sum(blocked[i][j]) > thresh:
                new[i][j] = 255
    return new

def last():    
    v = cv2.VideoCapture(0)
    s = 2
    thresh = 255*s*s*0.5
    while True:
        suc, img = v.read()  
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (1280, 720))
        st = time.time()
        new = func(img, 3)
        cv2.imshow("!", new)
        cv2.waitKey(1)

with Profile() as profile:
    print(f"{last() = }")
    (
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
    )
    


    

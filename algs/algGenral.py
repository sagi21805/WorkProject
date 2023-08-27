import cv2
import numpy as np
from abc import ABC
import numpy.lib.stride_tricks
from numba import njit, prange

class Img(ABC):

    def __init__(self, liveImg: np.ndarray, lenSize: int) -> None:
        self.img = liveImg
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.lenSize = lenSize
        self.pixelToMicro = 0.174 * self.lenSize
  
    def imgPrep(self, s):
        #TODO try avarage and than canny on window
        resized = cv2.resize(self.gray,  (1280, 720))  
        # filter = np.array([[-1, -1,  -1], 
        #                    [-1,  10, -1], 
        #                    [-1, -1,  -1]])
        
        # sharpend = cv2.filter2D(resized, -1, filter)
        blured = cv2.bilateralFilter(resized, 20, 75, 75)
        self.prepedImg = applyWindow(blured, s, (256, 360))
        self.markedImg = cv2.resize(self.img, (self.prepedImg.shape[1],self.prepedImg.shape[0]))
    
@njit(fastmath=True)
def applyWindow(img: np.ndarray, s, regions: tuple[int, int]):
    # thresholds = caluclateThreshold(img, regions)
    regionThreshold = 255*0.47
    blocked = numpy.lib.stride_tricks.sliding_window_view(img, (s, s))
    new = np.zeros((blocked.shape[0], blocked.shape[1]), np.uint8)
    for i in prange(len(blocked)):
        for j in prange(len(blocked[0])):
            # regionThreshold = thresholds[int(np.ceil(i // (img.shape[0] // regions[0])))][int(np.ceil(j // (img.shape[1] // regions[1])))]
            if (np.sum(blocked[i][j])) > (regionThreshold * s * s):
                new[i][j] = 255
    return new

# @njit(fastmath=True)
# def caluclateThreshold(img: np.ndarray, regions: tuple[int, int]):
#     """caluclate the threshold for the apply window func

#     Args:
#         img (np.ndarray): the input img for the apply window function
#         regions (tuple[x: int, y: int]): how many regions to devide the img in x and y``notice the the regions must be devideable by the img size (for each x and y)``
#     Returns:
#         thresholds (np.ndarray): array of the threshold per region 
#     """
#     print(img.shape)
#     if img.shape[1] % regions[0] != 0 or img.shape[0] % regions[1]:
#         raise Exception(f"the img regions is not devideable by the img \n {img.shape[1]} % {regions[0]} or {img.shape[0]} % {regions[1]} is not zero")
    
#     blocked = numpy.lib.stride_tricks.sliding_window_view(img, (img.shape[0] // regions[1], img.shape[1] // regions[0]))
#     thresholds = np.zeros((blocked.shape[0], blocked.shape[1]))
#     print(blocked.shape)
#     for i in prange(len(blocked)):
#         for j in prange(len(blocked[0])):
#             thresholds[i][j] = np.max(blocked[i][j]) * 0.9 + np.min(blocked[i][j]) * 0.1

#     return thresholds




    #TODO work on the threshold
    #TODO imporve software


        



    
        
    
import cv2
import numpy as np

def imgPrep(img):
    img = cv2.resize(img, (1269, 714))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (4,4))
    v = np.median(blur)
    sigma = 0.2
    lower_thresh = int(max(0, (1.0 - sigma) * v))
    upper_thresh = int(min(255, (1.0 + sigma) * v))
    canny = cv2.Canny(blur , lower_thresh ,upper_thresh)
    return canny


 
import numpy as np

a = np.array([[5, 5, 4, 4]])
b = np.array([[[4, 4], [3, 3]]])
d = np.array([3, 3])

a[a > 4] = 0
print(a)
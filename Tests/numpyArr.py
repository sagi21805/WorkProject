import numpy as np

arr1 = np.array([[1, 2, 3, 5, 5], 
                 [1, 5, 3, 5, 5], 
                 [1, 2, 3, 4, 5]])

arr2 = np.array([[1, 2, 3, 5], 
                 [1, 2, 3, 5], 
                 [1, 2, 3, 4]])

arr3 = np.array([])

np.append(arr3, arr2[0][0:3])
print(arr3)
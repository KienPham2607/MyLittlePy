import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[1])
print(arr[2] * arr[3])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, -1])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ndmin=4)
print(arr[0, 0, 1, -2])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Slice the array
print(arr[-5:])
# With specified step
print(arr[1:5:2])

arr = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)
print(arr[1, 1:4])

import numpy as np

# ------------------------
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))

# print(arr)

# # -------------------------
# # Joining 2-d array
# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis=2)

# print(arr)

# ----------------------------
# Joining array using stack function
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr3 = np.array([4, 5, 6])

arr1 = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)
arr2 = np.array(
    [
        [5, 6],
        [7, 8]
    ]
)
# arr = np.concatenate((arr1, arr2), axis=1)

arr = np.stack((arr1, arr2), axis=0)
print(arr)

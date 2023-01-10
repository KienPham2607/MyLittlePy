# Import numpy and Alias it
import numpy as np
import array as arr

print("\n---------------------------------")
print("Create numpy array and compare it to the normal one:")
#   -> Create a normal numpy array
# arr1 = np.array([1, 2, 3, 4, 5])
# print(f"\tNumPy array: {arr1}, its type: {type(arr1)}")

#     -> Compared with normal array
# arr2 = arr.array('i', [1, 2, 3, 4, 5])
# print(f"\tNormal array: {arr2}, its type: {type(arr2)}")

# ------------------------------- #
#   -> Create ndarray from array-like object
print("\n---------------------------------")
print("Create ndarray from array-like object:")
#   -> Normal array
# _arr = np.array(arr.array('i', [1, 2, 3, 4, 5]))
# print(f"\t{_arr}, its type {type(_arr)}")
# print(f"\t\t{_arr[0]}")

#   -> Tuple
# tpl = np.array(("Mot", "Hai", "Ba"))
# print(f"\t{tpl}, its type {type(tpl)}")
# print(f"\t\t{tpl[1]}")

#   -> 2-d and 3-d ndarrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2-d ndarray: {arr}, {arr.ndim}")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(f"3-d ndarray: {arr}, {arr.ndim}")
#   -> Set
# _set = np.array({"apple", "banana", "cherry"})
# print(f"\t{_set}, its type {type(_set)}")
# print(_set[0])
# IndexError: too many indices for array: array is 0-dimensional, but 1 were indexed

#   -> Dictionary
# _dict = np.array(
#     {
#         "brand": "Ford",
#         "model": "Mustang",
#         "year": 1964
#     }
# )
# print(f"\t{_dict}, its type {type(_dict)}")
# print(_dict[0])
# # IndexError: too many indices for array: array is 0-dimensional, but 1 were indexed

import array as arr

a = arr.array('i', [1, 2, 3, 10])
print(a)
# Modify an array's element
# a[1] = 5
b = a
c = b[0:]
print(c)
print()
# # Access elements in the array
# print("The items stored in array are:")
# for i in range(0, 4):
#     print(a[i])
# print()

# Insert a new element into array at specified position
print("Array after being inserted a new element")
a.insert(0, -9)
print(a)
print(b)
print()

# Remove and pop an element
a.remove(2)
print("Array after removing an element")
for i in a:
    print(i)
print()

print("Array after popping an element")
print(f"Popped element: {a.pop()}")
for i in a:
    print(i)
print()

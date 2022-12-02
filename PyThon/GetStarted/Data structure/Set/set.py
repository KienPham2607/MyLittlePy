# Print out a set
numberSet = {1, 2, 3, 4, 3, 2}
print(numberSet)

# Get type of {} to see if it is a set or dictionary
emptySet = {}  # This creates a dictionary
print(type(emptySet))

emptySet = set()  # This create an empty set
print(type(emptySet))

# A set can contain different data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# A set cannot store lists
# set_list = set([1, 2, 3, 4])
# print(type(set_))
# print(set_list)

# Remove an element from a set
my_set = {'Vietnam', 10, 19, 'Dong Trieu'}
print(my_set)
my_set.remove("BinhKhe")
print(my_set)

# Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Union           = {A | B}")
print(f"Intersection    = {A & B}")
print(f"Difference      = {A - B}")
print(f"Symmetric Diff  = {A ^ B}")

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8, 10}
print(odd.isdisjoint(even))
print(numbers.issuperset(odd))
print(odd.issuperset(numbers))
print(odd.issubset(numbers))

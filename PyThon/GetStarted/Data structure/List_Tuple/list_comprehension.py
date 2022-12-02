# Import required module
import time


# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result


# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]


# Driver Code

# Calculate time takens by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end-begin, 2))
print()
# Assign matrix
twoDMatrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]
print(trans)

# Initializing string
string = 'Geeks4Geeks'
# Toggle case of each character
List = list(map(lambda i: chr(ord(i) ^ 32), string))
# Display list
print(List)


# Example 7: Display the sum of digits of all the odd elements in a list.
# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
# Displaying new list
print(newList)

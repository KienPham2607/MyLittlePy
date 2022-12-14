# with open('py_digits.txt') as file_object:
# 	# contents = file_object.read()
# 	for line in file_object:
# 		print(line.rstrip())
# print("\n---------------------\n")
# for line in open('py_digits.txt'):
# 	print(line.rstrip())
print("\n---------------------\n")

with open('py_digits.txt') as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

print("\n---------------------\n")
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(pi_string[:20])
# print(len(pi_string))


filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()

birthday = '1910'
if birthday in pi_string:
	print("Your birthday exists")
else:
	print("Your birthday does not exist")
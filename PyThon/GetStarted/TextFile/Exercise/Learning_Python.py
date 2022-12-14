"""
Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block. 
"""
# file = open('learning_python.txt', 'a')

# n = int(input("Number of lines to be stored: "))
# for _ in range(0, n):
#     l = input("In Python you can: ")
#     print(f"In Python you can: {l}", file=file)
# file.close()

f = 'learning_python.txt'

print(f"\nreading in the entire file: \n{open(f, 'r').read()}\n")

print("looping over the file object:")
for line in open(f, 'r'):
    print(line.strip())

print(f"\nstoring the lines in a list:")
lines = [a_line.strip() for a_line in open(f, 'r')]
print(lines)

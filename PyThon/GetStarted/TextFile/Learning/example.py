# Reading text form file using list comprehension - vscode cannot read example.txt
import os
# print(os.listdir())
lines = [line.strip() for line in open('example.txt')]
print(lines)
# Alternative way
print(open('example.txt').read())

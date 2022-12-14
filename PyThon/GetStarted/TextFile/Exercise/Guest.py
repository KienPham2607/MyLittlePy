"""
    10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt
    """
file = 'guest.txt'
with open(file, 'a') as file_object:
    file_object.write(input("Enter your name: ") + "\n")

with open(file, 'r') as file_object:
    print(file_object.read())

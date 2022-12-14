"""
Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
    """
file_name = 'guest_book.txt'

is_continue = 'y'
with open(file_name, 'a') as file_object:
    while is_continue == 'y':
        user_name = input("Enter your name: ")
        file_object.write(f"{user_name}\n")
        print(f"Greeting: {user_name}")
        is_continue = input("Continue (y/n): ")

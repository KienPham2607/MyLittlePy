"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
    """

file_name = 'response.txt'
is_continue = 'y'
with open(file_name, 'a') as file_object:
    while is_continue == 'y':
        response = input("Why you like programming: ")
        file_object.write(f"{response}\n")
        is_continue = input("Continue (y/n): ")

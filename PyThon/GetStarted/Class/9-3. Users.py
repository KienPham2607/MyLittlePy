"""
    Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
    Create several instances representing different users, and call both methods
for each user.
    """


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}, wellcome to python")


wifi = User('anh', 'nguyen')
wifi.describe_user()
wifi.greet_user()

husband = User('kien', 'pham')
husband.greet_user()
husband.describe_user()

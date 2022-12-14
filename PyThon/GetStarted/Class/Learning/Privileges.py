"""
    Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
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


class Admin(User):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()


class Privilege:
    def __init__(self) -> None:
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


ad = Admin("Anh", "Ngoc")
ad.privileges.show_privileges()

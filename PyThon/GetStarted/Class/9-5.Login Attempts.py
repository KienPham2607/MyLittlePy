"""
    Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

    Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
    """


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0

    def describe_user(self) -> None:
        print(f"first name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self) -> None:
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}, wellcome to python")

    def increment_login_attempts(self) -> None:
        self.login_attempt += 1

    def reset_login_attempts(self) -> None:
        self.login_attempt = 0


wifi = User('anh', 'nguyen')
wifi.greet_user()

wifi.increment_login_attempts()
print(wifi.login_attempt)
wifi.increment_login_attempts()
print(wifi.login_attempt)
wifi.increment_login_attempts()
print(wifi.login_attempt)

wifi.reset_login_attempts()
print(wifi.login_attempt)

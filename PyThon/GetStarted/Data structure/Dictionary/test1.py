class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}, wellcome to python")


marks = {
    "Maths": 45,
    "Science": 43,
    "Social": 38,
    "DSA": 90,
    "SDLC": 80
}

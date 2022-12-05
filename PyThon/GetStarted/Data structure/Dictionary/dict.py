# """
# dictionary
#     """


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"first name: {self.first_name}, last name: {self.last_name}")

    def greet_user(self):
        print(
            f"Hello {self.first_name.title()} {self.last_name.title()}, wellcome to python")


a_dict = {
    'key1': 'value1',
    User("Trung", "Kien"): 'value2'
}
print(a_dict['key1'])
# print(a_dict[User("Trung", "Kien")]) key error cause User("Trung", "Kien") create a new instance
# print(a_dict)

marks = {
    "Maths": 45,
    "Science": 43,
    "Social": 38,
    "DSA": 90,
    "SDLC": 80
}
print(marks)

student = {
    "name": "",
    "age": 20,
    "birth": "19/10/2002"
}
print(student)
if "Maths" in marks:  # only for keys
    print(f"\n--Dictionary membership test: True")
print(f"\n--pop an arbitrary item: {marks.popitem()}")

print("\n--Iterating through a dictionary")
print("Get only key")

for subject in marks:
    print(subject)  # print key

print("\nGet both key and value")
for subject in marks:
    score = marks[subject]  # value
    print(f"{subject}: {score}")  # print key - value

print("\nAn alternative")
for subject, score in marks.items():
    print(f"{subject}: {score}")

print(f"\n--Keys: {marks.keys()}")
print(f"--Values: {marks.values()}")

marks.clear()
print(f"\n--Mark after being Cleared: {marks}")
# del student
# print(f"Del: {student}") #Throw name 'student' is not defined

print("\n--A dictionary stores object as value")
person = {
    "profile": User("Trung Kien", "Pham")
}
print(f"Print directly: {person}")
# a = person["profile"]
# print(f"Via key: {a}")
# print(f"The value: {a.first_name} {a.last_name}")
print(f"Via key: {person['profile']}")
print(
    f"The value: {person['profile'].first_name} {person['profile'].last_name}"
)
print("\n--A Dictionary stores list, set, tuple, and dictionary as value")
a_list = {
    "list": ["Trung", "Kien", "Pham"],
    "set": {"Pham", "Trung", "Kien"},
    "tuple": ("Kien", "Trung", "Pham"),
    "dict": {
        "name": "Pham Trung Kien",
        "Birth": "26/07/2002"
    }
}
x = a_list["list"][1]
print(f"-Access a list inside a dictionary: {x}")  # Worked

print("-Access a set inside a dictionary:")  # Worked
for item in a_list["set"]:
    print(f"\t{item}")

y = a_list["tuple"][2]
print(f"-Access a tuple inside a dictionary: {y}")  # Worked

z = a_list["dict"]["name"]
print(f"-Access a dictionary inside a dictionary: {z}")  # Worked

a = User("Anh", "Ngoc")
test = {
    1: a,
    2: a,
    1: a.first_name
}

a.last_name = "Nguyen"
print(test)

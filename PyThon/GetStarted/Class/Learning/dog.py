class Dog:
    """
    A simple attempt to model a dog
    """

    def __init__(self, name: str, age: int):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling over.")


my_dog = Dog("Moon", 3)
print(f"my dog's name is {my_dog.name}")
print(f"He is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
    """


class Restaurant:
    def __init__(self, res_name: str, cuisine_type: str):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> None:
        print(f"{self.res_name} serves {self.cuisine_type} dishes")

    def open_restaurant(self) -> None:
        print(f"{self.res_name} is opening")

    def set_number_served(self, number_served: int) -> None:
        self.number_served = number_served

    def increment_number_served(self, new_customers: int) -> None:
        self.number_served += new_customers


class IceCreamStand(Restaurant):

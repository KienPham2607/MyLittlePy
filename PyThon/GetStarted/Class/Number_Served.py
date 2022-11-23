"""
    Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
    Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
    Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
day of business.
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


a_beo = Restaurant("Grill House", "Vietnamese beef grilled")
a_beo.describe_restaurant()

a_beo.set_number_served(40)
print(a_beo.number_served)

a_beo.increment_number_served(3)
print(a_beo.number_served)

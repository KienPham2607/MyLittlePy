"""
    Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
    Make an instance called restaurant from your class. Print the two attributes 
individually, and then call both methods.
    """


class Restaurant:
    def __init__(self, res_name: str, cuisine_type: str):
        self.res_name = res_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.res_name} serves {self.cuisine_type} dishes")

    def open_restaurant(self):
        print(f"{self.res_name} is opening")


a_beo = Restaurant("Grill House", "Vietnamese beef grilled")
a_beo.open_restaurant()
a_beo.describe_restaurant()

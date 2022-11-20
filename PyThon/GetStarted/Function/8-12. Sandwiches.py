"""
    Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
    """


def take_topping(*items: str):
    print("Toppings I want on a sandwich: ")
    for item in items:
        print(f"\t-{item}")


take_topping("Love", "Kisses", "Hug")
take_topping("Lettuce", "Tomatoes", "Onion")

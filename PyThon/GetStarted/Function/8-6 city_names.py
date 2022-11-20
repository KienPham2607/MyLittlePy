"""
    Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
        "Santiago, Chile"
    Call your function with at least three city-country pairs, and print the values that are returned.
"""


def city_country(city: str, country: str):
    return f"{city}, {country}"


print(city_country("Hanoi", "Vietnam"))
print(city_country("Thai Nguyen", "Vietnam"))
print(city_country("Quang Ninh", "Vietnam"))

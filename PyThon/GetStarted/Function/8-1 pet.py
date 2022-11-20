def describe_pet(animal_type, pet_name):
    # or:    def describe_pet(animal_type: str, pet_name): add input data type
    # or:    def describe_pet(animal_type: str, pet_name="dog"): add default value
    """_summary_

    Args:
        animal_type (string): type of the animal
        pet_name (string): name of the pet
    """
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet("Dog", "Mun") # Positional Argument
describe_pet(pet_name="Dog", animal_type="Mun") # Keyword Argument

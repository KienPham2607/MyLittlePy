def make_shirt(size="Large", message="I love Python"):
    if size == "Large" or size == "Medium":
        print(f"size: {size} and the message: \"I love Python\"")
    else:
        print(f"size: {size} and the message: \"{message}\"")

make_shirt()
make_shirt("Medium",)
make_shirt("Small", "Love u")

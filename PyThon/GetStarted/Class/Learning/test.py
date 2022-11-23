class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

    def get_c(self):
        return self.__c

    def set_c(self, new_c):
        self.__c = new_c
# Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
# obj2 = Derived()

print(obj1.get_c())
obj1.set_c("Ngoc Anh")
print(obj1.get_c())

# will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class

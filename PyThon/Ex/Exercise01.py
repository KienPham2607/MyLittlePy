import array as arr


class Person:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def getName(self) -> str:
        return self.__name

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, new_address: str) -> None:
        self.__address = new_address

    def toString(self) -> str:
        return f"{self.__name.title()}\({self.__address.title()}\)"


class Student(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []
        self.__grades = arr.array("I", {})

    def toString(self) -> str:
        return f"Student: {super().toString()}"

    def addCourseGrade(self, course: str, grade: int) -> None:
        self.__courses.append(course)
        self.__numCourses += 1
        self.__grades.append(grade)

    def printGrade(self) -> None:
        # Research how to crreate string array
        pass

    def getAverageGrade(self) -> float:
        return sum(self.__grades) / self.__grades.itemsize

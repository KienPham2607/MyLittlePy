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
        return f"{self.__name.title()}({self.__address.title()})"


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
        for i in range(0, self.__numCourses):
            print(f"{self.__courses[i]}({self.__grades[i]})")

    def getAverageGrade(self) -> float:

        return sum(self.__grades) / len(self.__grades)


class Teacher(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__numCourses = 0
        self.__courses = []

    def toString(self) -> str:
        return f"Teacher: {super().toString()}"

    def addCourse(self, course: str) -> bool:
        if course in self.__courses:
            return False
        else:
            self.__courses.append(course)
            self.__numCourses += 1
            return True

    def removeCourse(self, course: str) -> bool:
        if course not in self.__courses:
            return False
        else:
            self.__courses.remove(course)
            self.__numCourses -= 1
            return True

    def getCourse(self):
        print(self.__courses)


a = Student("Ngoc Anh", "Trai Thong")
print("Student to string")
print(a.toString())

print("\nReAssgin address")
a.setAddress("Ninh Binh")
print(a.toString())

print("\nAddcourse and print grade")
a.addCourseGrade("Data structure and Algorithms", 8)
a.addCourseGrade("SDLC", 7)
a.printGrade()
print(f"Average grade: {a.getAverageGrade()}")

print('\nTeacher')
b = Teacher("Trung Kien", "Ninh Binh")
print(f"Teacher to string: {b.toString()}")
if b.addCourse("DSA"):
    print("Added successfully")
else:
    print("Addition failed")

b.addCourse("SDLC")
b.addCourse("Project web")
b.getCourse()
# Add duplicate
if b.removeCourse("DSA"):
    print("removed successfully")
else:
    print("remove failed")

b.getCourse()

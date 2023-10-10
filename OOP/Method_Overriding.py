class Student:
    def Display(self):
        print("This is Parent Class")

class Department(Student):
    def Display(self):
        super().Display()
        print("This is Child Class")

obj1 = Department()
obj1.Display()
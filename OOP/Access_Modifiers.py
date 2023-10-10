# class Employee:
#     def __init__(self):
#         self.__name = "Rutvik"

# obj = Employee()
# # print(obj.__name) # Cannot be accessed directly
# print(obj._Employee__name)  #   Can be accessed indirectly

class Student:
    def __init__(self):
        self._name = "Rutvik"
    
    def _funName(self):    # Protected Method
        return "Python Course"

class Subject(Student):     # inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())

# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     # def parent_method(self):
#     #     print("Abc")
#     #     super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rutvik","50")
harry = Programmer("Abc","1234","Python")

print(harry.name)
print(harry.id)
print(harry.lang)
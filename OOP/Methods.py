# Three methods for dir, __dict__, help

# a = (1,2,3)
# print(dir(a))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("Abc",22)
print(p.__dict__)
print(help(Person))
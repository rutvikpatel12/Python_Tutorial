class Person:
    name = "Rutvik"
    age = 21
    ocupation = "Software Developer"

    def info(self):
        print(f"{self.name} is a {self.ocupation}")

# -- Create Object
a=Person()
b=Person()
# -- Change name
# a.name = "Amit"
# print(a.name)
# print(a.age)
# print(a.ocupation)
a.info()

b.name = "Ankit"
b.info()
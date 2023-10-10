# --- PARENT CLASS
class Person:
    def __init__(self, name):
        self.name = name
    
    def Details(self):
        print(f"My name is {self.name}")

# --- CHILD CLASS
class Programmer(Person):
    def showLanguage(self):
        print("The default language is Python")

# -- run only parent class
# obj1 = Person("Rutvik Kamani")
# obj1.Details()

# --- both class run
obj2 = Programmer("Rutvik Kamani")
obj2.Details()
obj2.showLanguage()
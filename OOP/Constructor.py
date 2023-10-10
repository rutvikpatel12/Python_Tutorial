class Person:
    # --- DEFAULT CONSTRUCTOR
    # def __init__(self):
        # print("Called Default Constructor")

    # PARAMETERIZED CONSTRUCTOR
    def __init__(self, name, occ):
        # print("I am Developer")
        self.name = name
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("Ram","Developer")
b=Person("Shyam","Owner")
a.info()
b.info()

a.name = "Sahil"
a.occ = "Owner"
# a.info()
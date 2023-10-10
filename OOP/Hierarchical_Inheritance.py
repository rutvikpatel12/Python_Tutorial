class Company:
    def com(self):
        print("This is company class")

class Designer(Company):
    def des(self):
        print("This is Designer Class")

class Marketing(Company):
    def mar(self):
        print("This is Marketing Class")

obj1 = Designer()
obj2 = Marketing()

obj1.com()
obj1.des()

obj1.com()
obj2.mar()
class Parent():
    def dsp1(self):
        print("This is parent class")
    
class Child(Parent):
    def dsp2(self):
        print("This is child class")

obj = Child()
obj.dsp1()
obj.dsp2()
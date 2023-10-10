class Course:
    def cos(self):
        print("This Course is MCA")

class Subject1(Course):
    def sub1(self):
        print("I am learned from Python")

class Subject2(Course):
    def sub2(self):
        print("I am learned from Java")

class Subject3(Subject1, Subject2):
    def sub3(self):
        print("I am learned from Asp.Net")

obj = Subject3()
# obj.cos()
obj.sub1()
obj.sub2()
obj.sub3()
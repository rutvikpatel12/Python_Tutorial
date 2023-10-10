class College:
    def __init__(self, cname):
        self.cname = cname

class Department(College):
    def __init__(self, dname):
        self.dname = dname

class Course(Department):
    def __init__(self, cname, dname, coname):
        self.cname = cname
        self.dname = dname
        self.coname = coname

    def Display(self):
        print(f"My College name is {self.cname}")
        print(f"My Department name is {self.dname}")
        print(f"My Course name is {self.coname}")

obj = Course('RK','IT','MCA')
obj.Display()
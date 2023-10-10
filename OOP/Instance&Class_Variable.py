# Instance Variable VS Class Variable

class Employee:
    companyName = "Microsoft"
    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployee +=1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Rutvik")
emp1.raise_amount = 0.3
emp1.companyName = "Google"
emp1.showDetails()
Employee.companyName = "Dell"
print(Employee.companyName)
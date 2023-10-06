# There are four types of arguments that we can provide in a function:
# 1.  Default Arguments
# 2.  Keyword (Arbi) Arguments
# 3.  Variable length Arguments
# 4.  Required Arguments

# 1. Default
# def average(a=3,b=2):
# def average(a=3,b):
#     print("The average is",(a+b)/2)

# average()
# average(5)


# 2. Keyword
# def name(fname,mname="A",lname="Kamani"):
#     print("Hello",fname,mname,lname)

# name(lname="xyz",fname="abc")


# def calculate(a,b=5,c=6):
#     print("The Average is: ",a+b+c)

# calculate(10,54)


# Return Function
def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(5,3,4,2)
print("Average is: ",c)
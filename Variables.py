x=4     # global variable
# print(x)

def hello():
    # x=5     # local variable

    # modify the global variable
    global x
    x=10
    y=4
    print(f"The local y is {y}")

hello()
print(f"The global x is {x}")
# print(f"The local y is {y}")    # this will cause an error because y is a local variable and is not accessible outside of the function
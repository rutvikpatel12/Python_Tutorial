# def double(x):
#     return x*2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y: (x + y)/2

print(double(5))
print(cube(4))
print(avg(2,4))

# print(appl(cube, 2))
print(appl(lambda x: x*x*x, 2))
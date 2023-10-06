# # def cube(x):
# #     return x * x * x

# # print(cube(2))

# --- MAP
# l = [1,2,4,6,4,5]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# # --- FILTER
# def filter_function(a):
#     return a>4

# new1 = list(filter(filter_function, l))
# print(new1)


# --- REDUCE
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# -> Calculate the sum of the numbers using the reduce function

# sum = reduce(lambda x,y: x + y, numbers)

# -- Second method
def mysum(x, y):
    return x + y

sum=reduce(mysum,numbers)

# Print the sum
print(sum)
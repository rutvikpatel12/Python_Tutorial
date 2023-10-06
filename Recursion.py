def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# Fibonacci Sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n=int(input("Enter number: "))
print("Fibonacci is: ")
for i in range(n):
    print(fibonacci(i))
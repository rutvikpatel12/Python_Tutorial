def greet(fx):
    def modify(*args, **kwargs):
        print("Good afternoon")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return modify

# Add Decorators
@greet
def hello():
    print("Hello Friends")

def add(a,b):
    print(a+b)

hello()

# Second method for add -> Decorators
greet(add)(1,4)
a="!!Rutvik !!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))

print(a.replace("Rutvik","Tushar"))

intro="introduction to python"
print(intro.capitalize())

str1 = "Good Afternoon !!!"
print(len(str1))
print(len(str1.center(50)))

print(str1.endswith("!!!"))     # True
# print(str1.endswith("@@@"))     # False

str1 = "Welcome to the Python!!!"
print(str1.endswith("to",4, 10))

str1 = "My name is Rutvik, I am software developer."
print(str1.find("is"))
# print(str1.index("iss"))  # Show Error

str1="mynameisrutvik"
print(str1.isalnum())
str1="Welcome00"
print(str1.isalpha())

str1="Hello World"
print(str1.islower())

# str1="Hello How are you\n"    # False
str1="Hello How are you"        # True
print(str1.isprintable())

str1 = "        "
print(str1.isspace())

str1 = "Hello World"
print(str1.istitle())

str1 = "Hii Friends"
print(str1.startswith("Hii"))

str1 = "Hello World"
print(str1.swapcase())

str1 = "My name is rutvik kamani"
print(str1.title())


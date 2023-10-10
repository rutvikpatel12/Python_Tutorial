# Walrus Operator
# -> assign values to variables as part of a larger expression

# --- Simple type
# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)


# Walrus operator type
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
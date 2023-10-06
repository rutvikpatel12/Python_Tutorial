letter = "Hey My name is {} and I am from {}"
name="Rutvik"
city="Junagadh"

print(letter.format(name,city))
print(f"Hey my name is {name}, and I am from {city}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=14.2523666))

print(f"{6*3}")
print(type(f"{6*3}"))
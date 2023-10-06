dic = {
    "fname" : "Rutvik",
    "lname" : "Kamani",
    "age" : 21,
}

# Two mwthod for print value
# print(dic["fname"])
# print(dic.get("lname"))

# # Print all keys
# print(dic.keys())

# # Print all values
# print(dic.values())

# Print all Values using for
# for key in dic.keys():
#     print(f"The value is {dic[key]}")


# print key and value both
# print(dic.items())

# Print key and value both
for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
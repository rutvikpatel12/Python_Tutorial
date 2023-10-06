tpl=(1,54,13,8,"White",47.25,True)
# print(tpl)
print(len(tpl))
# print(tpl[1])
# print(tpl[5])
# print(tpl[53])    # Error

print(tpl[-2])

if 123 in tpl:
    print("Yes 123 is present tpl")
else:
    print("No 123 is not present tpl")

tpl2 = tpl[1:5]

# Slicing
# print(tpl2)   # Create New Tuple
city = ("Rajkot","Ahmedabad","Junagadh","Valsad")
state = ("Gujarat","Rajasthan","UP","Bihar")

# Concatinat Tuple
# mt = city + state
# print(mt)

# temp = list(city)
# temp.append("Surat")        # Add item
# temp.pop(2)                 # remove item
# temp[1] = "Gandhinagar"     # change item
# citys = tuple(temp)
# print(citys)

tpl1 = (1,23,5,8,5,2,36,5)
# res = tpl1.count(5)
# res = tpl1.index(36,2,7)
res = len(tpl1)
print("Count of 36 in tpl1 is: ",res)

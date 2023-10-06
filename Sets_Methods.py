s1 = {1,2,6,8,4}
s2 = {5,9,6,1}
set3 = {6,2,8}


# print(s1.union(s2))
# print(s1.intersection(s2))
# s2.intersection_update(s1)

# s1.update(s2)

# print(s1)

# s3=s1.symmetric_difference(s2)
# print(s3)

# s3 = s1.difference(s2)
# print(s3)

# print(s1, s2)
# print(s1.isdisjoint(s2))

# print(s1.issuperset(set3))

# print(set3.issubset(s1))

s1.add("Raj")
# print(s1)
# s1.update(s2)

s1.remove(8)
# s1.remove("Rk") # Error

s1.discard("RK")    # Not Error Show
# item = s1.pop()
# print(s1)
# print(item)

# del s2  # all item delete for set
# s1.clear()
print(s1)

# Check if item exists
if "Raj" in s1:
    print("Raj is present")
else:
    print("Raj is absent")
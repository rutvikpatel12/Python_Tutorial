l = [1,41,26,2,6,2,25,2]
print(l)

l.append(51)
# l.sort()  # Sort Ascending
# l.sort(reverse=True)  # Sort Decending
# l.reverse() # Reverse Original String

# print(l.index(26))
print(l.count(2))

m=l.copy()
# m[0] = 85
# print(l)
# print(m)

l.insert(2,855)
print(l)

a=[568,412,102]
c=a+l
# l.extend(a)
print(c)
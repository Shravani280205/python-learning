a = {1, 3, 4, 5, 1}
print(type(a))
print(a)

a= {}
print(type(a)) #print type as dictionary

#creating empty set
b = set()
print(type(b))


#Set Functions
b.add(4)
b.add(3)
b.add(4) # adding a value repeatedly does not change a set
b.add(5)
b.add(6)

# Length of the set
print(len(b))
print(b)

# Removal 
b.remove(5)
print(b)

# Pop
print(b.pop())


# Set Methods
c = {2, 3, 4, 234, 23, 43, 32, 12}
d = {2, 3, 233, 121, 22, 23, 455, 334}

# Union of the set - Combine all element in two set
print(c | d)

# Intersection of set - common in two set
print(c & d)






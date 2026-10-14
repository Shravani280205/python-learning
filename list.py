a=[1, 2, 3, 4, 5, 6]
print(a[5])
a[0]=98
print(a)


c=[45, "shravani", False, 6.9 ]
print(c)


#list slicing
friends=["Shravani", "Vaidehi", "Sakshi", "Janhvi", "Dimpal"]
print(friends[0:4])
print(friends[-4:1])

#list Methons 
l1 = [1, 8, 7, 2, 21, 15]
# l1_sorted = l1.sort()
# print(l1_sorted)
l1.sort()
print(l1)

l1.append(45) #adds at end of the list
l1.append(65) #adds at end of the list
l1.append(35) #adds at end of the list


l1.insert(2, 455) #insert 455 at index 2
print(l1)


l1.pop(2) #removes element at index 2
print(l1)


l1.remove(21) # removes element 21 from the list
print(l1)


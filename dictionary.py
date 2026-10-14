mydict = {
    "fast": "In a  Quick Manner",
    "Shravani": "Student",
    "Marks": [1,2,5,6],
    "Anotherdict": {'harry' : 'player'},
    1: 2121
}

print(mydict)
print(mydict['fast'])
print(mydict['Shravani'])
print(mydict['Marks'])
print(mydict['Anotherdict']['harry'])
print(mydict[1])


# Dictionary Methods 
print(mydict.keys())
print(mydict.values())
print(list(mydict.keys()))
print(list(mydict.values()))
print(mydict.items()) # print key value pairs in dictionary



#changing values of dictionary
mydict['Marks'] = [45,35,32,54]
print(mydict['Marks'])


print(mydict)
updatedict = {
    "Vaidehi" : "Friend"
} 

mydict.update(updatedict) # update the dictionary by adding key value pairs from updatedict

print(mydict)

print(mydict.get("Shravani2")) # Returns none as Shravani2 is not present in dictionary
# print(mydict["Shravani2"]) # throw an error as Shravani2 is not present in dictionary
print(mydict["Shravani"]) 


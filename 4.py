#4 types of data sets
#list[], dictionary, tuple{}, set() 

# Sets

myset = {"bananas","tomato","Potato","tomato"}
print(myset)   # any order printing is there

print(myset.__len__())    # print(len(myset))   

# set can be made by using constructor also

z =set(("apple","bananas","chiku"))
print(z)

print(type(z))

for x in z:
    print(x)


print("apple" in z)        # true

z.add("Priyam")
print(z)

# to concaetes two sets we hv to use update function 
y = {"Anmol","Priyam"}

z.update(y)                   # to add y and z in sets
print(z)

z.remove("Priyam")        # also    z.discard("Priyam")
print(z)

print(z.clear)
print(z.pop())

set1 ={1,2,3,4,5}
set2 ={4,0,3,9}

set3 = set1.union(set2)

print(set3)
set3 = set1.intersection(set2)
print(set3)

                                         # DICTIONARY
                                         
thisdict = {
    "Brand " : "Ford",
    "Mode " : 1234,
    # Dictionary syntax
    
    "color" : ["white","grey", "blue"] ,
    "year" : 1999
    # key : value
}  
# not allow multiple values
# dictionary always print in the order 

print(type(thisdict))                                  

print(len(thisdict))

print(thisdict["Brand "])           # get the value of the key 

print(thisdict)

print(thisdict.values())    # print the values
print(thisdict.keys())      # print the keys

x = thisdict.items()            #  keys will come in one bracket 
print(x)

if "tyre" in thisdict:
    print(True)
else:                                      # checks for the key
    print(False)

thisdict["year"] = 2021                    #  changing the value of the key

print(thisdict)

thisdict.pop("color")
print(thisdict)                          # deleted the color key

thisdict.popitem()                        # used to remove the last entered item in the dictionary

print(thisdict)

# del thisdict                            # to delete the whole dictionary
print(thisdict)                       # it shows error since dictionary is deleted

y = { "Name" : "Priyam",
     "Roll no." : 123
     }

y.clear()                        # here the elements are cleared but dictionary is prseent there only

print(y)

dic = {
    "Brand " : "Ford",
    "Mode " : 1234,
}

for x in dic:                         #For loop used to print the dictionary keys values
     print(dic[x])
    
for x in dic.values(): 
    print(x)                                          # prints keys values                                

for x,y in dic.items():             # print keys with values
    print(x,y)
    
dic1 = dic.copy()           # To copy the key and values of dictionary dic in another dictionary dic1
print(dic1)   
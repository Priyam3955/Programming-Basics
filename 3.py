# Error handelling

#1. Syntax error  -> Here we get error
#2. exception   -> here no problem in the execution part 

# when we know that find an error in something so write that in try syntax
try:
    x = 5 / 0
except :
    print("Error aaya tha")
    
    
try :
    x = 6 / 0                               #here only onlt try gives error then it will not go to another excptional handelling
    print(z)
except ZeroDivisionError:
    print("error tha" )
except variable:
    print("variable toh declare krley ")
finally:
    print("mein toh print honga")
    
    
                     #exceptional handelling using function
def func(a , b):
    try:
        c = ( a + b ) / ( a - b )
    except ZeroDivisionError:
        print("error")
    else:
        print(c)
    finally:
        print("Mein toh zarur chalunga")                  # This finally keyword is used always run whether above code will run or not
        
    func(3,2)
    func(3,3)
    
                                                 #TUPLES
    #tuple is a variable where we can store multiple data items
    # two ways to make a tuple
mytuple = ('priyam','anmol','raja')             #any value can be stored          # 1st way
print(mytuple)       

print(type(mytuple))

x = tuple((1,2,3,4))                          # 2nd way use two brackets 
print(x)

#once tuple is formed can not be changed

z = (1,2,3,4)
print(z) 

print(z[2])     #accesing values using index

print(len(z))       # to find the length of tuple

c = ("h")
print(type(c))  # it shows string so we have to use commas 

c = ("h",)
print(type(c))     #now shows tuple

y = (1,2,3,4,5,6,7,8,9)                #now comes negative indexing

print(y[-1])

print(y[-7:-1])

##
if 66 in y:
    print(True)
else:
    print(False)
    
# To change value in tuple indirectly

x = ("apple","Banana","Mango")
y = list(x)            # making list
y[1] = "kiwi"          # changes done
y.append(5)

# same thing used for removing things in the list
x = tuple(y)           # again make tuple
print(x) 

# we can add two tuples

z = ("Priyam",)
x = x + z
print(x)


# Packing and unpacking of the tuple

fruits = ("banana","orange","chiku")
(red, green, yellow) = fruits     # no. of variables initialized is eQual to the no of ientities in the tuple
print(red)
print(green)
print(yellow)

# loop in tuple
y =(1,2,3,4,2,2,5)
for x in y:      # to print all the values
    
    print(x) 
    
for x in range(0,5):
    print(y[x])                   # x is now acting as index values
    
# OR above can be solved as 
#for x in range(len(y)):
 #   print(y[x])
        
print(y.count(2))            # count the numbers of 2's
print(y.index(2))            # checing index number

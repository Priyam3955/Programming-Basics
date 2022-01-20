# File handling
 # To store the data in file using programme 
 # by using file handling operations
 
# Make a txt folder for e.g pep.txt made in folder
file = open("pep.txt","r")    # r represent read mode mein

# there are 4 types of functions 
# read, write, either both, append

print(file.readline())     # To print the first line of the txt and enter the line

print(file.read())          # prints the all data 

print(file.readline())       # prints blank since its pointer is next to the third line

file.seek(0)               # seek function is used to take pointer to any index as given in the brackets

print(file.readline())

print(file.tell())                    # prints the line number

with open("pep.txt") as file:        # print the data using with keyword
    print(file.read())
    
# NOw write function to make changes in txt file from the program

file1  = open("pep.txt","w")
file1.write("I'm Machine learning enthusiast")
#file1.close()           ## this is very important without this result with no changes in the txt file
  # Chnages occured in the txt file
  
# file1.tell()            # we hv to comment the close function while caliing the file1 items

file1.seek(34)                 # to get the pointer at that index value
file1.write("TUV")
file1.close()

## OBJECT ORIENTED

class myclass:
    x =5             #DATA mambers or properties 
     
p1  = myclass              # Object
print(p1.x)                # prints the object

# Now make a init function

class person:                  #Parent class
    def __init__(self,name,age):      #we can give dodo inplace of self or anything
        self.name = name         # now change the self by 
        self.age = age         # this is init function i.e assign the properties
         
    def myfunc(self):
        print("My friend is Priyam " + self.name)
          

# p1 is simply a variable it become an object when when we give class to it as person and 
# init function call itself.
    
p1 = person("Priyam", 14)       # Creating objects e.g p1 and assigning the properties to the object
                                # without person declaration in p1, p1 is only a variable 
print(p1.name)
print(p1.age)   
p1.myfunc()        

p1.age = 40

print(p1.age)

del p1      # to delete the object

# print(p1.age)       # error since object is deleted hence shows an error

class something:
    pass            # pass is keyword to blank the code 

                             # Inheritance
                             
class person:          # Parent function
    def __init__(self, fname,lname):
        self.firstname = fname   #first name is the properties and f name is the paramater
        self.lastname = lname                             
             
    def printname(self):
        print(self.firstname,self.lastname)
         
x = person("Aman" , "Dubey")      
x.printname()                  # error comes when we gave spaces in the starting 

class student(person):       # don't forget to give the arguments
    pass

y = student("Shinchan","Nohara")
y.printname()                     # this is called inheritance

# class student(person):       # don't forget to give the arguments
#     def __init__(self, fname, lname):
#      pass                                                   # now error shows in the printing part
#                                               # since __init__ function is initialized 
# y = student("Shinchan","Nohara") 
# y.printname()                     # this is called inheritance

class student(person):     # Child class  # don't forget to give the arguments
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)    # here print function works since we have called person init

y = student("Shinchan","Nohara")
y.printname()                     # this is called inheritance

class student(person):     # Child class  # don't forget to give the arguments
    def __init__(self, fname, lname):
        super().__init__(fname, lname)    # here print function works since we have called person init
        self.graduationyear = 2019
 #   --->   super class defined here
y = student("Shinchan","Nohara")
y.printname()                     # this is called inheritance callin gfunction from the parent class
print(y.graduationyear)     #this is printing the properties of the object y from the given properties 
                            # in the class.




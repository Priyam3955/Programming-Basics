a =10
def s():    #*Use of functions 
    global a     #* Assign global variables
    a =20
    
print(a)
s()
print(a)

#* To print data types such as int , float , bool
print(type(a))

c = 2<3
print(c)       #* printing bool types whether true or false 

#* strings

e = "This is my country"
print(type(e))
print(len(e))

#* slicing
print(e[2])

print(e[0:5])                  #* from 0 to 5 index value print the string 
print(e[0:14:2])               #* to skip the string by 2 character

#* negative indexing or negative slicing

print(e[::-1])        #* Will print in reverse order 
                    #* indexing done from last as -1 to first character in negative numbers 
print(e[-1:-13])

print(e.capitalize())
print(e.lower())

print(e.count('t'))

print(e.endswith('country'))   #* print the true or false whtether string is ending or not
print(e.find('t'))

#* there are many inbuilt funcions like this, check it from internet.
                                          #*  FUNCTIONS
                                
def func1():
    print("this is me func1")
    
func1()     
#* we can call as many times this function and at anywhere 
#* 1. Builtin functions 
#* 1. User defined functions 

def sum(a,b):
    '''This func is used to find sum '''        #* This is called doxing and is used to find the working of the function
    c =a+b
    print(c)       #* return and print both will print the values
    return c       #* understand the meaning of return statement much important 
print(sum(2,4))
print(sum.__doc__)     #* To find anywhere the working of the function

                                                 #* CONDITIONAL AND LOOPS 
      #* 1. Conditionals - if else, elif , nested if else 
a = int(input())
if(a>10):
     print("Yes! Number is greater than 10")
else:
 print("Number is less than 10")
 
#*                                                     #* USE OF ELIF
if(a>10):
 print("Yes! Number is greater than 10")
elif (a<5):
    print("NUmber is less than 5")
else:
 print("Number is less than 10")
        
                                                        #* NESTED IF ELSE 
if(a>10):
     print("Yes! Number is greater than 10")
     if(a>20):
         print("YEs")
else:
 print("Number is less than 10")
 
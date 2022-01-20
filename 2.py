   #* LOOPS
  #* Repeat condition and comes outside the loop when condition fails  
count = 0
while(count<3):
    print("This is me")
    count = count + 1
     
     #* here if is not present 
else:
    print("Comes outside the loop")
    
              #* FOR LOOP
for i in range(0,10):             #* By using range keyword
    print(i)                      #* Print the numbers from 0 to 9

li = 'First','Second','Third'

for i in li:       #* here it means just take the alues from li and print all the values
    print(i)
    
#* NESTED LOOPS

for i in range(2,5):
    for j in range(0,i):            #* Just same as like when condition fails then go outside the loop
        print(i , j)
                                
                                #* Use of break and pass 
q = 'Priyam'                                
for i in q:
    print(i)
    if(i == 'r'):
        break
print("Outside the loop")

a = 'Anmol'
for i in a:
    pass                      #* Pass used to left for loop as it is means blank      

print("outside ")

#* USe of continue statement 

d ='Gupta'
for i in d:
    if(i == 'G'):
        continue                     #* Continue is used to say that once again now go to the loop without
    print(i)                         #* without printing the loop content downwards
    
print("out of the loop")
   #* 7 things are left 

                                  #* List data types
#* dynamically sized array
 
li1 = [1,2,3,4]
li2 = [4,3,2,1]
print(li1 == li2)     #* LIST see the sequencing of order in which list

li3 =['Priyam', 1,2,3,4]    #* In list any thing can be placed 
print(li3,li2)       

print(len(li3))       #* print the length of the list 

li4 = ['Priyam',1,2,3,4]         # Slicing concept in list data type
print(li4[0:4])

print(li4[::-1])                         # Reverse the list 

print(li4[-1])            # so here in negative indexing, it is to be done from the last, for e.g. index -1 is to be done for value as 4

print(li4[-1:-5:])                # it will print from index = -1 to index = -4 i.e up to n - 1 values

li4.append('appended')         # to add one more data in the list
print(li4)

li4.insert(0, 22234)     #replace the value at index = 0 with 22234
print(li4)

li1.extend(li4)
print(li1)              # add the two or more lists 

print(li4.pop())                 # remove the element from the list 
print(li4)

print(li4.pop())    # agin applied pop operation
  
li4.remove(3)         # To remove the element, element will be removed which is in the close bracket
print(li4)

x1 = [x**2 for x in range(1,10)]                   #last topic is link comprehension
print(x1)                               # here print the sQuare of 1 to 9 numbers 


       
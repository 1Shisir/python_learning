# print("Aashis")
# x = input("'say your name:")
# print(f"hello {x}")



# x = int(input("Enter one number:"))
# y = int(input("Enter second number:"))

# z = x+y

# print(f"The sum of {x} and {y} is {z}")

# x= int(input("Enter a number:"))
# if(x%2 == 0):
#     print("Even")
# else:
#     print("Odd")    


# x=  int(input("Enter  1st numbers"))
# y=  int(input("Enter  2st numbers"))
# z=  int(input("Enter  3st numbers"))

# if(x>y and x>z):
#     print(f"{x} is greater")
# elif(y>x and y>z):
#     print(f"{y} is greater")
# else:
#     print(f"{z} is greater")        

#program to print even numbers less than 20

# for i in range(1,21):
#     if(i%2 == 0):
#         print(i)
#     else:
#         pass

#add at least 5 students in a list and print those numes ends with a or A
#mylist = [ "Aashisa", "Ramesh", "Suresh", "Rajesha", "Rajeshwari"]
# for name in mylist:
#     if(name[-1] == "a" or name[-1] == "A"):
#         print(name)

#add at least 5 students in a list and print those names whose length is greater than or eqauls to 5
# mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]
# for name in mylist:
#     if(len(name) >= 5):
#         print(name)


#WAP to ask the names of 5 students from the user and store them in a list and print the name of students whose starting from a or A
# mylist = []
# for i in range(5):
#     x = input("Enter the name:")
#     mylist.append(x)
# for name in mylist:
#     if(name[0] == "A" or name[0] == "a"):
#         print(name)    

#WAP to ask the index and data with the user ad insert the data at the given index
# mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]
# index = int(input("Enter the index:"))
# data = input("Enter the data:")
# mylist.insert(index, data)
# print(mylist)

# print("9815335428  Binay Adhakari")

# mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]
# del mylist[2]
# print(mylist) 


# mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]
# mylist.remove("Ram")
# print(mylist) 


# mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]
# input = int(input("Enter the index to remove:"))
# del mylist[input]
# print(mylist) 

#mylist = ["Aashisa", "Ram", "Suresh", "esha", "Rajesh"]

# input = input("Enter the name to remove:")
# try:
#     mylist.remove(input)
#     print(mylist)
# except:
#     print("Name not found")    


# mylist[0] ="Shisir" 
# print(mylist)

#print 1 to 10 using while loop
# i =1
# while(i<=10):
#     print(i)
#     i+=1

#print even numbers less thsn 20 using while loop

# i = 0
# print("Even numbers less than 20 are:")
# while(i<=20):
#     if(i == 0):
#         pass
#     elif(i%2 == 0):
#         print(i)
#     i+=1


#wap to ask the user with the names of student and dtore to a list, ask the names until the name entered by user ends with a or A.Print all the names
#mylist = []
# while True:
#     x = input("Enter the name:")
#     if(x[-1] == "a" or x[-1] == "A"):
#         mylist.append(x)
#         break
#     else:
#         mylist.append(x)
# print(mylist)    


# name = ' '
# while name[-1] != "a" and name[-1] != "A":
#     name = input("Enter the name:")
#     mylist.append(name)
# print(mylist)



#wap to ask user to enter two number and operation to be performed on them. Perform the operation and print the result

# def get_data():
#     num1 = int(input("Enter the first number:"))
#     num2 = int(input("Enter the second number:"))
#     operation = input("Enter the operation to be performed:")
#     if operation == '+':
#         print(f"Addition of {num1} and {num2} is {num1+num2}")
#     elif operation == '-':
#         print(f"Subtraction of {num1} and {num2} is {num1-num2}")
#     elif operation == '*':
#         print(f"Multiplication of {num1} and {num2} is {num1*num2}")
#     elif operation == '/':
#         print(f"Division of {num1} and {num2} is {num1/num2}")
#     else:
#         print("Invalid operation")
#     return
# get_data()   

#WAP to print the sum of all the arguments passed to the function without using sum() function
# def get_data(*args):
#     res = 0
#     for a in args:
#         res =  res + a
        
#     print(res)
# get_data(2,3) 
# get_data(2,3,4,5,6)  

def welcome(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")
    return
  
welcome(name='sodha', age=23, city='kathmandu')
welcome(name='sodha', age=23, city='kathmandu', country='nepal')


try:
    # code that may raise an exception
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter a valid number")        
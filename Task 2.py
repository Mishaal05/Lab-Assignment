Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number=-1
>>> if number>=0:
...     print("Number is positive")
... else:
...     print("Number is negative")
... 
...     
Number is negative
>>> year=int(input("Enter a year:"))
Enter a year:2025
>>> if(year %400==0):
...     print("It's a leap year")
... else:
...     print("It's not a leap year")
... 
It's not a leap year
>>> num1=int(input("Enter number:"))
Enter number:2
>>> num2=int(input("Enter number:"))
Enter number:4
>>> operator=input("Enter operator (+, -, *, /):")
Enter operator (+, -, *, /):+
>>> if operator == "+":
...     result=num1+num2
...     print(result)
... elif operator == "-":
...     result=num1-num2
...     print(result)
... elif operator == "*":
...     result=num1*num2
...     print(result)
... elif operator == "/":
...     result=num1/num2
...     print(result)
... else:
...     print("Invalid Operator")
... 
6

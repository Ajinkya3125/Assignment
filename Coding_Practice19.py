# Q1)Write a Python program to find the square root of a number using the math module.
import math
num = int(input("Enter the number:"))
result = math.sqrt(num)
print(f"Square root of {num} =",result)


#Q2)Write a Python program to find the factorial of a number using the math module.
import math
num = int(input("Enter the number:"))
result = math.factorial(num)
print(f"Factorial of {num} =",result)


# #Q3)Write a Python program to find the value of:π × r²
import math
radius = int(input("Enter the value of radius:"))
result = math.pi*radius*radius
print("Area of circle:",result)


# Q4)Write a Python program to generate a random number between:
import random

result = random.randint(1, 100)
print(result)


# Q5)Write a Python program to randomly select one name from:
lst = ["Ajinkya", "Rahul", "Amit", "Priya"]
result = random.choice(lst)
print(result)


# Q6)Write a Python program to simulate rolling a dice.
import random

dice_value = random.randint(1, 6)
print("Dice Value:", dice_value)


# Q7)Write a Python program to display the current working directory.
import os
print("Current Directory:", os.getcwd())


# Q8)Write a Python program to create a new folder named:
import os
os.mkdir("PythonPractice")
print("Folder created successfully")


#Q9)Write a Python program to check whether a file named:
import os
print(os.path.exists("data.txt"))


#Q10)Write a Python program to display the current date and time.
import datetime
current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))


#Q11)Write a Python program to display only the current year.
import datetime
current_year = datetime.datetime.now()
print(current_year.strftime("%Y"))


#Q12)Write a Python program to find the number of days between:
from datetime import datetime

date1 = input("Enter first date(Y-m-d):")
date2 = input("Enter second date(Y-m-d):")

d1 = datetime.strptime(date1,"%Y-%m-%d")
d2 = datetime.strptime(date2,"%Y-%m-%d")

print("Number of daye:",abs((d2 - d1).days))


#Q13)Import only the sqrt() function from the math module and find:
from math import sqrt
num = int(input("Enter the number:"))
result = sqrt(num)
print(result)


#Q14)Import only the choice() function from the random module and select a random fruit from:
from random import choice
lst = ["Apple", "Mango", "Banana"]
result = choice(lst)
print(result)


#Q15)Create your own module named:
# calculator.py and define functions:
# add()
# subtract()
# multiply()
# Then import the module into another Python file and use all three functions.
#Main.py
import calculator as cal
print(cal.add(2,3))
print(cal.subtract(3,4))
print(cal.multiply(4,5))

# calculator.py
def add(n1,n2):
    return n1 + n2
    
def subtract(n1,n2):
    return n1 - n2
    
def multiply(n1,n2):
    return n1 * n2


#Q16)Write a Python program that displays:
# Current Date
# Current Time
# Current Working Directory
# using appropriate modules.
import datetime
import os
current_date = datetime.datetime.now()
print(current_date.strftime("%Y-%m-%d"))
current_time = datetime.datetime.now()
print(current_time.strftime("%H:%M:%S"))
print(os.getcwd())


# Q17)Generate a random password of 6 digits using the random module.
import random
random_password = random.randint(100000,999999)
print(random_password)


#Q18)calculate a factorial using user define modules
#Main.py
import calculator as cal
print(cal.facto(5))

# calculator.py
def facto(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact
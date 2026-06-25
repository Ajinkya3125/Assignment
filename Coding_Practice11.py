# #Q1)Write a function find_max(a, b, c) that returns the largest among three numbers.
# def find_max(a,b,c):
#     largest = max(a,b,c)
#     print(largest)
    
# find_max(10,25,18)


# #Q2)Write a function using *args that returns the sum of all numbers passed to it.
# def add_numbers(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(total)
# add_numbers(10, 20, 30, 40)


# #Q3)Write a function using **kwargs to print student information.
# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# student_info(name="Ajinkya",age=21,city="Pune")
    
    
# #Q4)Write a recursive function to find the factorial of a number.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = 5
# print(f"Factorial of {n} : {factorial(n)}")


# #Q5)Write a recursive function to calculate the sum of first n natural numbers.
# def sum_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_n(n-1)
# print(sum_n(5))


# #Q6)Write a recursive function to print numbers from 1 to n.
# def print_numbers(n):
#     if n == 0:
#         return 0
#     print_numbers(n-1)
#     print(n)
# print_numbers(5)


# #Q7)Write a Python program to create a file named sample.txt and write:
# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)
    
    
# #Q8)Write a Python program to count the number of lines in a text file.
# cnt = 0
# with open("sample.txt","r") as file:
#     for data in file:
#         cnt += 1
# print("Total number of lines :",cnt)


# #Q9)Write a Python program to handle a ZeroDivisionError.
# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Error:Cannot divide by zero")
    
    
# #Q10)Write a Python program to handle a ValueError when converting user input to an integer.
# try:
#     n = input("Enter the value:")
#     num = int(n)
# except ValueError:
#     print("Invalid Input")


# #Q11)Create a class Student with attributes:
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print(f"Name : {self.name},Age : {self.age}")
    
# s = Student("Ajinkya",21)
# s.display()


# #Q12)Create a class Rectangle with methods:
# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length * self.width
        
#     def perimeter(self):
#         return 2 * (self.length + self.width)
        
# rect = Rectangle(10,5)
# print("Area of rectangle:",rect.area())
# print("Perimeter of rectangle:",rect.perimeter())


# #Q13)Use a lambda function to find the larger of two numbers.
# larger_num = lambda x,y : max(x,y)
# print("Largest number:",larger_num(10,20))

# #Q14)Use lambda and map() to convert a list of temperatures from Celsius to Fahrenheit.
# lst = [0, 20, 30]
# result = list(map(lambda c : (c * 9/5) + 32, lst))
# print(result)


#Q15)Write a Python program to check whether a number is an Armstrong number.
num = int(input("Enter the number:"))
original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10
    
if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
#Q16)Write a Python program to find the missing number in a list.
lst = [1,2,3,5]    #first approach
n = len(lst) + 1
expected_sum = n * (n+1) // 2
actual_sum = sum(lst)

missing_num = expected_sum - actual_sum
print(missing_num)


lst = [1,2,3,5]    #second approach
for i in range(1,max(lst) + 1):
    if i not in lst:
        print("Missing Number:",i)
        break
    
    
#Q17)Write a Python program to find duplicate elements in a list.
lst = [1,2,2,3,4,4,5]    ##first approach
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)


lst = [1,2,2,3,4,4,5]    ##second approach
duplicates = []
freq = {}

for l in lst:
    freq[l] = freq.get(l,0) + 1

for key, value in freq.items():
    if value > 1:
        duplicates.append(key)
print(duplicates)


#Q18)Write a Python program to check whether two strings are rotations of each other.
s1 = "abcd"
s2 = "cdab"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("string are rotations of each other")
else:
    print("string are not rotations of each other")
    
    
#Q19)Write a Python program to find the first repeating element in a list.
lst = [10,20,30,20,40,10]

for num in lst:
    if lst.count(num) > 1:
        print("First repeating element:", num)
        break
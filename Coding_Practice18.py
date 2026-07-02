#Q1)Write a Python program to find the difference between the largest and smallest element in a list.
lst = [12, 5, 30, 18, 9]  #first approach
diff = max(lst) - min(lst)
print(diff)

large_num = lst[0]   #second approach
small_num = lst[0]
for l in lst:
    if l > large_num:
        large_num = l
        
    if l < small_num:
        small_num = l
        
print(large_num - small_num)


#Q2)Write a Python program to find the sum of all even elements in a tuple.
tup = (1, 2, 3, 4, 5, 6)
total = 0
for t in tup:
    if t % 2 == 0:
        total += t
print(total)


#Q3)Write a Python program to find all keys whose values are divisible by 5.
dic = {"A":10, "B":12, "C":25, "D":18}  #first approach
result = []
for key, value in dic.items():
    if value % 5 == 0:
        result.append(key)
print(result)

results = [key for key,value in dic.items() if value % 5 == 0]  #second approach
print(results)


#Q4)Write a Python program to find elements that are present in either set but not in both.
A = {1,2,3,4}
B = {3,4,5,6}
print(A.symmetric_difference(B))


#Q5)Write a Python program to count the number of consonants in a string.
string = "Python"
cnt = 0
vowel = "aeiouAEIOU"
for s in string:
    if s.isalpha() and s not in vowel:
        cnt += 1
print(cnt)


#Q6)Write a function is_prime(n) that returns:True if the number is prime, otherwise:False
def is_prime(num):
    if num <= 1:
        return False
        
    for i in range(2,num):
        if num % i == 0:
            return False
            
    return True
print(is_prime(4))


#Q7)Write a function using *args to return the sum of squares of all numbers passed.
def sum_squares(*args):
    total = 0
    for a in args:
        total += a**2
    print(total)
sum_squares(2,3,4)


#Q8)Write a function using **kwargs to print only those key-value pairs whose value is an integer.
def show(**kwargs):
    for key,value in kwargs.items():
        if isinstance(value, int):
            print(f"{key} : {value}")
show(name="ABC", age=21, city="Pune", marks=85)


#Q9)Write a recursive function to calculate:
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)
print(recursive_sum(5))


#Q10)Write a Python program to count the number of lines in a file.
cnt = 0
with open("data.txt","r") as file:
    for line in file:
        cnt += 1
print(cnt)


#Q11)Write a Python program that handles:
# ZeroDivisionError
# ValueError
# TypeError
# using separate except blocks.
try:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    result = n1 / n2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter the valid number")
except TypeError:
    print("Type Error")
    
    
#Q12)Create a class Rectangle with:
# length
# width
# Method : area()
# which returns : length * width
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
rec = Rectangle(20,10)
print(rec.area())


#Q13)Use lambda and map() to convert a list of temperatures from Celsius to Fahrenheit.
lst = [0, 20, 30]
result = list(map(lambda f:(f*9/5) + 32,lst))
print(result)


#Q14)Use lambda and filter() to extract all palindrome strings from a list.
words = ["madam", "python", "level", "java"]
result = list(filter(lambda x:x[::-1] == x,words))
print(result)


#Q15)Write a Python program to find the second most frequent character in a string.
string = "programming"
for s in string:
    if string.count(s) > 1:
        print(s)
        break
    
    
#Q16)Write a recursive function to convert a decimal number into binary.
def decimal_to_binary(num):
    if num <= 1:
        return str(num)
    else:
        return decimal_to_binary(num // 2) + str(num % 2)
print("Decimal to Binary :",decimal_to_binary(6))


#Q17)Create a class Student with:
# name
# marks
# Method:grade()
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def grade(self):
        if self.marks >= 75:
            print("Distinction")
        elif self.marks >= 60:
            print("First Class")
        elif self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

std = Student("ABC",60)
std.grade()


#Q18)OTP verification Code
import random

random_number = random.randint(100000,999999)
print(random_number)

user_enter = int(input("Enter the OTP:"))

if random_number == user_enter:
    print("OTP verified Successfully!")
else:
    print("Please enter valid OTP!")
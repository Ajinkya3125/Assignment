#Q1)Write a Python program to find the second smallest element in a list.
lst = [10, 5, 20, 3, 15]
smallest = float('inf')
second_smallest = float('inf')

for num in lst:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print("second smallest number:",second_smallest)


#Q2)Write a Python program to find all duplicate elements in a list.
lst = [1,2,3,2,4,5,4]
dup = []
for l in lst:
    if l not in dup and lst.count(l) == 2:
        dup.append(l)
print(dup)


#Q3)Write a Python program to count how many times each element appears in a tuple.
tup = (1,2,2,3,1,2)
freq = {}
for t in tup:
    freq[t] = freq.get(t,0) + 1
print(freq)


#Q4)Write a Python program to sort a dictionary by values.
dic = {"A":50,"B":20,"C":80}
result = dict(sorted(dic.items(), key=lambda item:item[1]))
print(result)


#Q5)Write a Python program to merge two dictionaries and add values of common keys.
d1 = {"A":10,"B":20}
d2 = {"B":30,"C":40}
d3 = d1.copy()

for key, value in d2.items():
    if key in d3:
        d3[key] += value
    else:
        d3[key] = value
print(d3)


#Q6)Write a Python program to find the symmetric difference between two sets.
A = {1,2,3}
B = {3,4,5}
print(A.symmetric_difference(B))


#Q7)Write a Python program to check whether two strings are anagrams.
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")
    
    
#Q8)Write a Python program to find the first repeated character in a string.
str1 = "abcaef"
for s in str1:
    if str1.count(s) == 2:
        print(s)
        break
    
#Q9)Create a list of all numbers from 1 to 100 that are divisible by both 3 and 7.
result = [n for n in range(1,101) if n % 3 == 0 and n % 7 == 0]
print(result)

#Q10)Write a function that returns the number of uppercase, lowercase, and digits in a string.
def count_case(str1):
    cnt = 0
    upper = lower = digit = 0
    for ch in str1:
        if ch.isdigit():
            digit += 1
        elif ch.isupper():
            upper += 1
        else:
            lower += 1
    print("Total digit:",digit)
    print("Total Uppercase:",upper)
    print("Total Lowercase:",lower)
count_case("PyThOn123")


#Q11)Write a function using *args that returns the product of all numbers passed.
def multiply(*args):
    prod = 1
    for a in args:
        prod *= a
    print(prod)
multiply(2,3,4)


#Q12)Write a function using **kwargs that returns the key having the maximum value.
def student(**kwargs):
    max_key = max(kwargs, key=kwargs.get)
    return max_key
print(student(math=90, science=95, english=85))


#Q13)Write a recursive function to reverse a number.
def reverse_number(num):
    if num < 10:
        return str(num)
    else:
        return str(num % 10) + reverse_number(num // 10)
print(reverse_number(1234))


#Q14)Write a recursive function to find the sum of digits at even positions.
def sum_digits(num_str,pos=1):
    if not num_str:
        return 0
    if pos % 2 == 0:
        return int(num_str[0]) + sum_digits(num_str[1:], pos+1)
    else:
        return sum_digits(num_str[1:], pos+1)
print(sum_digits(str(123456)))


#Q15)Write a Python program to count how many times the word "Python" appears in a file.
cnt = 0
with open("data.txt","r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.strip(".,!?") == "Python":
                cnt += 1
print(cnt)


#Q16)Write a Python program that handles:
# ZeroDivisionError
# ValueError
# using multiple except blocks.
try:
    num = int(input("Enter the number:"))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value")
    
    
#Q17)Create a class Employee with:
# Attributes:name and salary
# Method:annual_salary()
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def annual_salary(self):
        return self.salary * 12
        
emp = Employee("ABC",60000)
print(emp.annual_salary())


#Q18)Create a class Calculator with methods:
# add()
# subtract()
# multiply()
# divide()
# Create an object and perform all operations.
class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
        
    def multiply(self):
        return self.num1 * self.num2
        
    def divide(self):
        return self.num1 / self.num2
        
cal = Calculator(2,3)
print(cal.add())
print(cal.subtract())
print(cal.multiply())
print(cal.divide())


#Q19)Use lambda and sorted() to sort a list of strings according to their length.
lst = ["python","c","java","javascript"]
result = sorted(lst, key = lambda x:len(x))
print(result)


#Q20)a)Use filter() to keep only even numbers.
    #b)Use map() to square them.
numbers = [1,2,3,4,5,6,7,8,9,10]
even_num = filter(lambda x : x % 2 == 0, numbers)
result = list(map(lambda x:x**2,even_num))
print(result)


#Q21)Write a Python program to find the longest common prefix among a list of strings.
strings = ["flower","flow","flight"]
prefix = strings[0]
for word in strings[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
print("Longest common prefix:",prefix)


#Q22)Write a Python program to check whether a string contains only unique characters.
string = "python"
is_unique = True
for s in string:
    if string.count(s) > 1:
        is_unique = False
        break
print(is_unique)


#Q23)Create a class Student that stores marks of 3 subjects and calculates:
# Total
# Average
# Grade
# using methods.
class Student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def total_marks(self):
        return self.m1+self.m2+self.m3
    
    def average(self):
        return self.total_marks() / 3
        
    def grade(self):
        avg = self.average()
        
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'D'
            
std = Student(89,90,87)
print("Total Marks:",std.total_marks())
print("Average:",std.average())
print("Grade:",std.grade())
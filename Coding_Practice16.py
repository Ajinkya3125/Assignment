#Q1)Write a Python program to find the last non-repeating character in a string.
string = "aabbcdeff"
for s in reversed(string):
    if string.count(s) == 1:
        print(s)
        break
    
    
#Q2)Create a class Mobile with:
# brand
# price
# Create a method display() that prints the mobile details.
class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        
    def display(self):
        return f"Brand : {self.brand} \nPrice : {self.price}"
        
mob = Mobile("Samsung",20000)
print(mob.display())


#Q3)Use lambda and map() to convert a list of numbers into their squares.
lst = [2,3,4,5]
result = list(map(lambda x:x**2,lst))
print(result)


#Q4)Write a Python program to find the key with the minimum value in a dictionary.
dic = {"A":50,"B":20,"C":80}     ##first approach
min_key = None
min_value = float('inf')
for key, value in dic.items():
    if value < min_value:
        min_value = value
        min_key = key
print(min_key)

dic = {"A":50,"B":20,"C":80}     ##second approach
min_key = min(dic, key=dic.get)
print(min_key)


#Q5)Write a recursive function to find the sum of all odd numbers from 1 to n.
def sum_odd(num):
    if num == 0:
        return 0
    
    if num % 2 != 0:
        return num + sum_odd(num-1)
    else:
        return sum_odd(num-1)
print(sum_odd(7))


#Q6)Write a Python program to check whether a given string is a pangram.
# A pangram contains every letter of the alphabet at least once.
sentence = "The quick brown fox jumps over the lazy dog"

if len(set(sentence.lower()) - set(" ")) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
    
    
#Q7)Use lambda and filter() to extract all numbers that are multiples of 3 from a list.
lst = [3,5,6,8,9,12,15]
result = list(filter(lambda x : x % 3 == 0,lst))
print(result)


#Q8)Create a class Laptop with:
# brand
# ram
# Create a method upgrade_ram(extra_ram) that increases the RAM.
class Laptop:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
        
    def upgrade_ram(self,extra_ram):
        self.ram += extra_ram
        
    def display(self):
        return f"Brand : {self.brand} \nRAM : {self.ram} GB"
        
laptop = Laptop("HP",8)
print(laptop.display())

laptop.upgrade_ram(8)

print(laptop.display())


#Q9)Write a Python program that takes two numbers as input and handles:
# ValueError
# ZeroDivisionError
# while performing division.
# try:
#     n1 = int(input("Enter first number:"))
#     n2 = int(input("Enter second number:"))
#     result = n1 / n2
#     print(result)
# except ValueError:
#     print("Value error occured.....")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
    
    
#Q10)Write a Python program to check whether all elements in a tuple are unique.
tup = (1, 2, 3, 4, 5, 3)
if len(tup) == len(set(tup)):
    print("All elements are unique")
else:
    print("All elements are not unique")
    

#Q11)Write a recursive function to find the sum of squares of first n natural numbers.
def sum_squares(num):
    if num == 0:
        return 0
    else:
        return num**2 + sum_squares(num-1)
print(sum_squares(4))


#Q12)Write a Python program to find the third largest element in a list.
lst = [10, 50, 20, 40, 30]
first = second = third = float('-inf')
for num in lst:
    if num > first:
        third = second
        second = first
        first = num
    elif num > second:
        third = second
        second = num
    elif num > third:
        third = num
print("Third largest number:",third)
    
    
#Q13)Write a Python program to find the longest word in a sentence without using max().
sentence = "Python programming is very interesting"
words = sentence.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest Word:",longest_word)


#Q14)Write a Python program to create a new dictionary containing only the even values from a dictionary.
dic = {"A":10, "B":15, "C":20, "D":25}
result = {key:value for key,value in dic.items() if value % 2 == 0}
print(result)

#Q15)Write a function using *args to count how many numbers are greater than 50.
def count_greater(*args):
    cnt = 0
    for a in args:
        if a > 50:
            cnt += 1
    print(cnt)
count_greater(10, 60, 80, 25, 90)


#Q16)Use lambda and sorted() to sort a list of tuples based on the first element.
lst = [(5,2), (1,9), (3,4), (2,7)]
result = sorted(lst, key = lambda x:x[0])
print(result)

#Q17)Create a class Student with:
# name
# marks
# Create a method result() that returns:"Pass" if marks ≥ 40, otherwise:Fail
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
std = Student("ABC",39)
std.result()


#Q18)Write a recursive function to find the sum of all even numbers from 2 to n.
def sum_even(num):
    if num == 0:
        return 0
        
    if num % 2 == 0:
        return num + sum_even(num-1)
    else:
        return sum_even(num-1)
print(sum_even(10))
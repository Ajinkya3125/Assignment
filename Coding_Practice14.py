#Q1)Write a function count_even(numbers) that takes a list as input and returns the count of even numbers.
def count_even(lst):
    cnt = 0
    for l in lst:
        if l % 2 == 0:
            cnt += 1
    print(cnt)
count_even([1,2,3,4,5,6])


#Q2)Write a function using *args to return the average of all numbers passed.
def average_sum(*args):
    total = 0
    n = len(args)
    for a in args:
        total += a
    return total / n
print(average_sum(10,20,30,40))


#Q3)Write a function using **kwargs to count how many key-value pairs were passed.
def count_items(**kwargs):
    cnt = 0
    for key, value in kwargs.items():
        if key:
            cnt += 1
    print(cnt)
count_items(name="ABC", age=21, city="Pune")


#Q4)Write a recursive function to find the product of digits of a number.
def product_digits(num):
    if num == 0:
        return 1
    else:
        return (num % 10) * product_digits(num // 10)
print(product_digits(234))


# #Q5)Write a Python program to append the text:
# with open("data.txt","a") as file:
#     content = "Welcome to Python"
#     file.write("\n" + content)
    
    
#Q6)Write a Python program to count the number of vowels present in a file.
cnt = 0
vowel = "aeiouAEIOU"
with open("data.txt","r") as file:
    for line in file:
        for ch in line:
            if ch in vowel:
                cnt += 1
    print("Number of vowels:",cnt)
    
    
#Q7)Write a Python program to handle a TypeError.
try:
    10 + "5"
except TypeError:
    print("Type mismatch error")
    
    
#Q8)Create a class Person with:
# name
# age
# Create a method is_adult() that returns: True,if age is 18 or above, otherwise-False
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
p = Person("ABC",18)
print(p.is_adult())
        
        
#Q9)Use a lambda function to calculate the cube of a number.
cube = lambda n : n ** 3
print(cube(4))


#Q10)Use lambda and filter() to extract all strings whose length is less than 5.
lst = ["python","cat","java","sql","go"]
result = list(filter(lambda l : len(l) < 5,lst))
print(result)


#Q11)Write a recursive function to find the largest digit in a number.
def largest_digits(num):
    if num < 10:
        return num
    else:
        return max(num % 10 ,largest_digits(num // 10))
print("Largest Number:",largest_digits(58291))


#Q12)Create a class Car with:
# brand
# model
# Create a method display() that prints the car details.
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display(self):
        return f"Brand : {self.brand} \nModel : {self.model}"
        
car = Car("Toyota","Fortuner")
print(car.display())


#Q13)using filter() function
lst = [1, 0, 2, None, 3, "", 4]
clean_data = list(filter(None, lst))
print(clean_data)
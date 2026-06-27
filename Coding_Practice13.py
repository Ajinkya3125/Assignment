#Q1)Write a recursive function to reverse a string.
def reverse_string(string):
    if string == "":
        return ""
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string("python"))


#Q2)Create a class BankAccount with methods:
# deposit()
# withdraw()
# display_balance()
# Demonstrate all three operations using an object.
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Cash deposited: {amount}")
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Cash withdrawn: {amount}")
        else:
            print("Insufficient Balance")
    
    def display_balance(self):
        print(f"Current Balance: {self.balance}")
        
account = BankAccount(10000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(500)
account.display_balance()


#Q3)Write a function count_vowels(text) that returns the total number of vowels in a string.
def count_vowels(string):
    vowel = "aeiouAEIOU"
    cnt = 0
    for ch in string:
        if ch in vowel:
            cnt += 1
    return cnt
print(count_vowels("Education"))


#Q4)Write a function using *args to return the smallest number among all arguments passed.
def smallest_num(*args):
    return min(args)
print(smallest_num(25, 10, 45, 5, 18))


#Q5)Write a function using **kwargs that prints all key-value pairs.
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
show_details(name="Ajay", age=21, city="Nashik")


#Q6)Write a recursive function to find the sum of digits of a number.
def sum_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_digits(num // 10)
print(sum_digits(12345))


#Q7)Write a Python program to count the number of characters in a file (excluding spaces).
cnt = 0
with open("data.txt","r") as file:
    for line in file:
        for ch in line:
            if ch != " " and ch != "\n":
                cnt += 1
print("Number of characters:",cnt)


#Q8)Write a Python program to handle an IndexError.
try:
    lst = [10,20,30]
    print(lst[5])
except IndexError:
    print("Index out of range")
    
    
#Q9)Create a class Circle with:
# radius
# Methods: area()
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
        
c = Circle(7)
print(c.area())


#Q10)Use a lambda function to find whether a number is divisible by 5.
result = lambda n : "True" if n % 5 == 0 else "False"
print(result(5))


#Q11)Use lambda and map() to add 10 to every element in a list.
lst = [5,10,15,20]
result = list(map(lambda x : x + 10,lst))
print(result)

#Q12)Write a recursive function to count the number of digits in a number.
def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num // 10)
print(count_digits(98765))


#Q13)Create a class Book with:
# title
# author
# Create two objects and display their details.
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def display(self):
        return f"Title : {self.title} \nAuthor : {self.author}\n"
        
book1 = Book("C programming","Denis Ritchie")
book2 = Book("Python Programming","Guido van Rossum")

print(book1.display())
print(book2.display())
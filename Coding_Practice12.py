#Q1)Write a function is_even(num) that returns:True-if the number is even, otherwise:False
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(8))


#Q2)Write a function using *args to find the largest number among all arguments passed.
def largest_num(*args):
    return max(args)
print(largest_num(10, 25, 5, 40, 18))


#Q3)Write a function using **kwargs that prints only the values passed to it.
def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}")
display(name="Ajinkya", age=21, city="Pune")


#Q4)Write a recursive function to find the power of a number.
def power(n,p):
    if p == 0:
        return 1
    else:
        return n * power(n, p-1)
print(power(2,4))


#Q5)Write a Python program to:
#i)Create a file named data.txt
#ii)Write the text:
# iii)Close the file.
cnt = 0
with open("data.txt","r") as file:
    for line in file:
        words = line.split()
        cnt += len(words)
print("Number of words:",cnt)


#Q6)Write a Python program to handle a KeyError.
try:
    student = {"name":"ABC"}
    print(student["age"])
except KeyError:
    print("Key not found")
    
    
#Q7)Create a class Employee with:
# employee_name
# salary
# Create an object and display the details.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        return f"Name : {self.name} \nSalary : {self.salary}"
        
emp = Employee("Raj",50000)
print(emp.display())


#Q8)Use a lambda function to check whether a number is positive or negative.
result = lambda n : "positive" if n > 0 else "Negative"
print(result(-5))


#Q9)Use lambda and filter() to extract all numbers greater than 50 from a list.
lst = [20, 55, 40, 80, 10, 90]
result = list(filter(lambda n : n > 50, lst))
print(result)
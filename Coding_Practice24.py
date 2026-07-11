#Part A: Inheritance
#Single Inheritance
#Q1)Create a class Animal with a method: sound()
# Create a child class Dog that inherits from Animal and calls the sound() method.
class Animal:
    def sound(self):
        print("Animal makes a sound.")
    
class Dog(Animal):
    pass

dog = Dog()
dog.sound()


#Q2)create Animal class and override the speak() method.
class Animal:
    def speak(self):
        print("Animal makes a sound.")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
    
cat = Cat()
cat.speak()


#Q3)create a Person class with name and create Student class with roll_no. 
# Use super() to initialize the parent class.
# Display both values.
class Person:
    def __init__(self,name):
        self.name = name
        
class Student(Person):
    def __init__(self,name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        
    def display(self):
        print(f"Name: {self.name} \nRoll No: {self.roll_no}")
        
std = Student("Ajinkya",251)
std.display()


#Q4)Multilevel Inheritance
class Person:
    def __init__(self,name):
        self.name = name
        
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
        
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
        
man = Manager("Ajinkya",120000,"IT")
man.display()


#Q5) Hierarchical Inheritance
class Vehicle():
    def start(self):
        print("Vehicle started")
        
class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass
        
bike = Bike()
bike.start()

car = Car()
car.start()

vehicle = Vehicle()
vehicle.start()


#Part B: Polymorphism
#Q6)Method Overriding
import math

class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
        
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
        
circle = Circle(5)
rectangle = Rectangle(10,4)

print("Area of Circle:",round(circle.area(),2))
print("Area of Rectangle:",round(rectangle.area(),2))


#Q7)Same Method, Different Objects
class Dog:
    def sound(self):
        print("Bark")

class Cat():
    def sound(self):
        print("Meow")

class Cow():
    def sound(self):
        print("Moo")

animals = [Dog(),Cat(),Cow()]
for a in animals:
    a.sound()
    
    
#Q8)Operator Polymorphism
# Demonstrate that:
# works differently for:
# integers
# strings
# lists
a = 10
b = 20
print(a + b)

str1 = "Hello "
str2 = "World"
print(str1 + str2)

lst1 = [10,20,30]
lst2 = [40,50,60]
print(lst1 + lst2)


#Part C: Encapsulation
#Q9)Private variable
class Student:
    def __init__(self,marks):
        self.__marks = marks
        
    def display_marks(self):
        print("Marks:",self.__marks)
        
student = Student(90)
student.display_marks()


#Q10)Getter and Setter
class Employee:
    def __init__(self):
        self.__salary = 0
        
    def set_salary(self,salary):
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
        
emp = Employee()
emp.set_salary(5000)
print("Salary:",emp.get_salary())


#Q11)Create a private variable: __password
#Try accessing it directly.
#Observe what happens.
#Then access it using a getter method.
class UserData:
    def __init__(self,password):
        self.__password = password
        
    def get_data(self):
        return self.__password
        
user = UserData("Pune@1234")
print(user.get_data())


#Part D: Abstraction
#Q12)Create an abstract class: Shape
# with abstract method: area()
# Create child class: Square
# Implement the method.
from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
        
class Square(Shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side**2
        
square = Square(5)
print("Area of Square:",square.area())


#Q13)Create abstract class: Vehicle
# Methods: start() and stop()
# Create child class: Car
# Implement both methods.
from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car strated")
        
    def stop(self):
        print("Car stopped")
        
car = Car()
car.start()
car.stop()


#Q14)Student Result System
class Person:
    def __init__(self,name):
        self.name = name
        
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks
        
    def result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")
            
std = Student("ABC",70)
std.result()


#Q15)Banking System
class BankAccount:
    def __init__(self,acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        
class SavingAccount(BankAccount):
    def __init__(self,acc_no,balance):
        super().__init__(acc_no,balance)
        
    def deposit(self,amount):
        self.balance += amount
        print(f"{self.balance} Credited Successfully")
        
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.balance} withdraw successfully")
        else:
            print("Insufficient Balance")
            
    def display(self):
        print(f"Account Number:{self.acc_no}")
        print(f"Balance:{self.balance}")
        
sacc = SavingAccount(101,10000)
sacc.deposit(500)
sacc.deposit(5000)
sacc.withdraw(2000)
sacc.display()


#Q16)multilevel inheritance.
class Animal:
    def eat(self):
        print("Animal eats food")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")
        
puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.weep()


#Q17)Method Overriding
class Employee:
    def work(self):
        print("Employee works")
        
class Developer(Employee):
    def work(self):
        print("Developer works")
    
class Tester(Employee):
    def work(self):
        print("Tester works")
        
class Manager(Employee):
    def work(self):
        print("Manager works")
  
developer = Developer()
tester = Tester()
manager = Manager()

developer.work()
tester.work()
manager.work()
##classes and objects
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

p = Person("Ajinkya")
p.greet()


##Encapsulation
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def credit(self, amount):
        self.__balance += amount
        return self.__balance
        
    def debit(self, amount):
        self.__balance -= amount
        return self.__balance
        
    def get_balance(self):
        return self.__balance

b = Bank(10000)
print("Credited amount:",b.credit(500))
print("Debited total amount:",b.debit(3000))
print("Total balance:",b.get_balance())


##Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


##Polymorphism
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

a = Dog()
a.speak()


##Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area of circle:", c.area())


##Magic methods(__init__, __str__)
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person name is {self.name}"

p = Person("Ajinkya")
print(p)



##super keyword
class Parent:
    def __init__(self):
        print("Parent class executed...")
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class executed...")
    
c = Child()


##constructor
class Student:
    def __init__(self,name):
        self.name = name
    
s = Student("Ajinkya Shinde")
print(s.name)


##method overloading-:
#1)using default argument
class Calculator:
    def add(self,a,b,c=1):
        return a + b + c
        
cal = Calculator()
print(cal.add(2,3))
print(cal.add(3,5,6))


##2)using *args
class Calculator:
    def add(self,*args):
        return sum(args)
        
cal = Calculator()
print(cal.add(2,3))
print(cal.add(2,3,4))
print(cal.add(2,3,4,5))
#Q1)Create a decorator that prints: "Before Function Execution" before calling a function.
def decorator(func):
    def wrapper():
        print("Before Function Execution")
        func()
    return wrapper
    
@decorator
def greet():
    print("Hello world")
    
greet()


#Q2)Create a decorator that prints:
# Function Executed Successfully
# after a function runs.
def decorator(func):
    def wrapper():
        func()
        print("Function Executed Successfully")
    return wrapper
    
@decorator
def greet():
    print("runs properly...")
greet()


#Q3)Create a decorator that prints:
# Starting...
# before execution and:
# Finished...
# after execution.
def decorator(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")
    return wrapper
    
@decorator
def greet():
    print("Learning Python")
greet()


#Q4)Write a decorator that works with a function that accepts one argument.
def decorator(func):
    def wrapper(name):
        func(name)
        print("Hello " + name)
    return wrapper
    
@decorator
def greet(name):
    print("Calling Function...")
greet("ABC")


#Q5)Create a decorator that can work with any number of positional arguments using *args.
def decorator(func):
    def wrapper(*args):
        print("Function Called")
        return func(*args)
    return wrapper

@decorator
def add(*args):
    total = 0
    for a in args:
        total += a
    return total
    
print(add(10,20,30))


#Q6)Create a decorator that can work with keyword arguments.
def decorator(func):
    def wrapper(**kwargs):
        print("Executing Function...")
        return func(**kwargs)
    return wrapper
    
@decorator
def show(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
show(name="ABC",age=21)


#Q7)Create a decorator that prints:
# Function Started
# before execution and:
# Function Ended
# after execution.
# Apply it to a function that prints numbers from 1 to 5.
def decorator(func):
    def wrapper():
        print("Function Started")
        func()
        print("\nFunction Ended")
    return wrapper

@decorator
def print_numbers():
    for i in range(1,6):
        print(i, end= " ")
print_numbers()


#Q8)Create a decorator that prints the name of the function being called.
# Example:
# Calling function: greet
def decorator(func):
    def wrapper():
        print("Calling Function:",func.__name__)
        func()
    return wrapper
    
@decorator
def greet():
    print("Hello!")
greet()


#Q9)Create a decorator that counts how many times a function is called.
def decorator(func):
    cnt = 0
    def wrapper():
        nonlocal cnt
        cnt += 1
        func()
        print(f"Called {cnt} times")
    return wrapper
    
@decorator
def hello():
    pass
hello()
hello()
hello()
hello()


#Q10)Create a decorator that prints:
# Multiplication Started
# before executing a multiplication function.
def decorator(func):
    def wrapper(n1,n2):
        print("Multiplication Started")
        return func(n1,n2)
    return wrapper

@decorator
def multiply(n1,n2):
    return n1 * n2
print(multiply(5,4))


#Q11)Create a decorator that converts the returned string into uppercase.
def decorator(func):
    def wrapper():
        return func().upper()
    return wrapper
    
@decorator
def greet():
    return "hello"
print(greet())


#Q12)Create a decorator that doubles the result returned by a function.
def decorator(func):
    def wrapper():
        return func() * 2
    return wrapper
    
@decorator
def double_result():
    return 10
print(double_result())


#Q13)Create a decorator Use two decorators on the same function.
def before_decorator(func):
    def wrapper():
        print("Before")
        func()
    return wrapper
    
def after_decorator(func):
    def wrapper():
        func()
        print("After")
    return wrapper
    
@before_decorator
@after_decorator
def greet():
    print("Hello")
greet()


#Q14)Create a decorator that checks whether a number passed to a function is positive.
def decorator(func):
    def wrapper(num):
        if num > 0:
            return func(num)
        else:
            print("Number must be positive")
    return wrapper
    
@decorator
def show_number(num):
    print("Number is positive")
show_number(-5)


#Q15)Create a decorator that prints:
# Admin Access Granted
# before executing a function named:
# delete_user()
def admin_access(func):
    def wrapper():
        print("Admin Access Granted")
        func()
    return wrapper
    
@admin_access
def delete_user():
    print("User deleted successfully...")
delete_user()


#Q16)Create a decorator that reverses the string returned by a function.
def decorator(func):
    def reverse_string():
        return func()[::-1]
    return reverse_string

@decorator
def greet():
    return "python"
print(greet())


#Q17)Create a decorator that squares the result returned by a function.
def decorator(func):
    def squares_num():
        return func() ** 2
    return squares_num
@decorator
def greet():
    return 5
print(greet())
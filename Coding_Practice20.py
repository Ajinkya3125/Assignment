#Q1)Create an iterator from the following list using iter() and print all elements using next().
lst = [10, 20, 30, 40]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#Q2)Create an iterator from a string and print each character using next().
s = "Python"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#Q3)Create an iterator for:
# lst = [1,2,3]
# Use next() repeatedly and handle the StopIteration exception.
lst = [1,2,3]
it = iter(lst)
try:
    while True:
        print(next(it))
except StopIteration:
    print("End of Iterator")
    
    
#Q4)Write a generator function that yields numbers from 1 to 5.
def numbers():
    for i in range(1,6):
        yield i
    
for num in numbers():
    print(num)
    

#Q5)Write a generator that yields all even numbers from 2 to 20.
def even_numbers():
    for i in range(2,21):
        if i % 2 == 0:
            yield i
        
for num in even_numbers():
    print(num, end= " \n")
    
    
#Q6)Write a generator function that yields the squares of numbers from 1 to 10.
def squares_num():
    for i in range(1,11):
        yield i * i
    
for num in squares_num():
    print(num)
    
    
#Q7)Write a generator that yields each character of a string one by one.
string = "HELLO"
def string_print():
    for i in string:
        yield i

for s in string_print():
    print(s)
    
    
#Q8)Write a generator function to generate the first n Fibonacci numbers.
def fibonnaci(n):
    a, b = 0, 1
    
    for _ in range(n):
        yield a
        a,b = b,a+b
n = 7
for num in fibonnaci(n):
    print(num)
    
    
#Q9)Write a generator that performs a countdown from n to 1.
def countdown(n):
    for i in range(n,0,-1):
        yield i
        
n = 7
for num in countdown(n):
    print(num)
    

#Q10)Create an iterator for the tuple:
tup = (100, 200, 300, 400)
it = iter(tup)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#Q11)Write a generator that yields odd numbers between 1 and 25.
def odd_numbers():
    for i in range(1,26):
        if i % 2 != 0:
            yield i
            
for num in odd_numbers():
    print(num)
    

#Q12)Convert the following list comprehension into a generator expression:
# squares = [x*x for x in range(1,6)]
# Print all generated values.
def squares_num():
    for i in range(1,6):
        yield i * i

for num in squares_num():
    print(num)
    
    
#Q13)Create an iterator for the keys of a dictionary and print them using next().
dic = {"name":"ABC","age":21,"city":"Pune"}
it = iter(dic)
print(next(it))
print(next(it))
print(next(it))


#Q14)Write a generator that yields the digits of a number one by one.
num = 12345
def number_digits():
    for i in str(num):
        yield i
    
for num in number_digits():
    print(int(num))
    
    
#Q15)Write a generator that yields all multiples of 5 up to 50.
def multiple_five():
    for i in range(5,51):
        if i % 5 == 0:
            yield i
    
for num in multiple_five():
    print(num, end= " ")
    
    
#Q16)Create an infinite generator that continuously yields:
def infinite_generator():
    num = 1
    while True:
        yield num
        num += 1
    
gen = infinite_generator()

for _ in range(10):
    print(next(gen))
    
    
#Q17)Write a generator that yields prime numbers up to n.
def prime_num(n):
    for num in range(2,n+1):
        is_prime = True
        
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num

for p in prime_num(20):
    print(p)
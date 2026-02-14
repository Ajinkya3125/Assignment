##Lambda Function
##1. addition of two numbers
add = lambda a, b: a + b
print(add(5, 3))


##2. Square of a number
square = lambda x: x * x
print(square(5))


##3. Check even or odd
even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even(4))


##4. Multiply three numbers
mul = lambda a, b, c: a * b * c
print(mul(2, 3, 4))


##5. Using map() (apply function to all elements)
lst = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, lst))
print(result)

##6. Using filter() (filter elements)
lst = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, lst))
print(result)


##7. Using sorted() with lambda
lst = [(1, 5), (2, 3), (4, 1)]
result = sorted(lst, key=lambda x: x[1])
print(result)


##8. Find maximum using lambda
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))


##9. Sort dictionary by values
d = {"a": 3, "b": 1, "c": 2}
result = sorted(d.items(), key=lambda x: x[1])
print(result)


##10. Sort strings by length
words = ["python", "is", "easy", "language"]
result = sorted(words, key=lambda x: len(x))
print(result)


##11. Filter names starting with vowel
names = ["Ajay", "Ravi", "Ankit", "Kiran"]
result = list(filter(lambda x: x[0].lower() in "aeiou", names))
print(result)


##12. Multiply each element by index
lst = [10, 20, 30]
result = list(map(lambda x: x[0] * x[1], enumerate(lst)))
print(result)


##13. Sort list of dictionaries by age
students = [
    {"name": "A", "age": 23},
    {"name": "B", "age": 20},
    {"name": "C", "age": 25}
]

result = sorted(students, key=lambda x: x["age"])
print(result)


##14. Find numbers greater than average
lst = [10, 20, 30, 40]
avg = sum(lst) / len(lst)
result = list(filter(lambda x: x > avg, lst))
print(result)
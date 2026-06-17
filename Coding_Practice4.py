#Q1)Write a Python program to count how many times a number appears in a list.
num = [1,2,3,2,4,2]
n = int(input("Enter the number to count:"))
print(num.count(n))

#Q2)Write a Python program to convert a tuple into a list.
tup = (1,2,3,4)
print(list(tup))

#Q3)Write a Python program to add a new key-value pair to a dictionary
dic = {"name":"ABC"}
dic["age"] = 21
print(dic)

#Q4)Write a Python program to find the difference between two sets.
set1 = {1,2,3,4}
set2 = {3,4,5}
print(set1 - set2)
print(set1.difference(set2))

#Q5)Write a Python program to convert a string into uppercase.
s = "python"
print(s.upper())

#Q6)Write a Python program to find all even numbers from a list.
num = [1,2,3,4,5,6]
even = [n for n in num if n % 2 == 0]
print(even)

#Q7)Write a Python program using list comprehension to create a list of cubes from 1 to 10.
cube = [n**3 for n in range(1,11)]
print(cube)

#Q8)Write a Python program to count the frequency of numbers in a list using a dictionary.
num = [1,2,2,3,1,4,2]
freq ={}
for n in num:
    freq[n] = freq.get(n,0) + 1
print(freq)

#Q9)Write a Python program to check whether two sets are equal.
A = {1,2,3}
B = {3,2,1}
print(A == B)


#Q10)Write a Python program to count uppercase and lowercase characters in a string.
str1 = "PyThOn"
lowercase = uppercase = 0
for s in str1:
    if s.islower():
        lowercase += 1
    elif s.isupper():
        uppercase += 1
print("Lowercase:",lowercase)
print("Uppercase:",uppercase)
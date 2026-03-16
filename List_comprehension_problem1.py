#1)Write a Python program using list comprehension to create a list of squares from 1 to 10.
lst = [1,2,3,4,5,6,7,8,9,10]
square = [x**2 for x in lst]
print(square)

#2)Write a program using list comprehension to create a list of even numbers from 1 to 20.
lst = [1,2,3,4,5,6,7,8,9,10]
even = [n for n in lst if n % 2 == 0]
print(even)

#3)Write a Python program to convert a list of strings into uppercase using list comprehension.
string = ["hello","world","apple","coconut"]
upper = [ch.upper() for ch in string]
print(upper)


#4)Write a program to remove negative numbers from a list using list comprehension.
lst = [-1,0,-2,5,7,-5,-3,6,1,-4]
remove_negative = [n for n in lst if n >= 0]
print(remove_negative)


#5)Write a program to extract only vowels from a string using list comprehension.
string = "hello world"
vowel = ['a','e','i','o','u']
extract_vowel = [v for v in string if v in vowel]
print(extract_vowel)


#6)Write a program to create a list of odd numbers from 1 to 20 using list comprehension.
odd_number = [n for n in range(1,21) if n % 2 != 0]
print(odd_number)


#7)Write a Python program to convert a list of integers into strings using list comprehension.
num = [1,2,3,4,5]
list_to_string = [str(s) for s in num]
print(list_to_string)


#8)Write a Python program to create a list of cubes of numbers from 1 to 10.
cube = [x**3 for x in range(1,11)]
print(cube)

#9)Write a Python program to create a list of numbers divisible by 5 from 1 to 50.
divisible = [d for d in range(1,51) if d % 5 == 0]
print(divisible)

#10)Write a program to extract each character from a string into a list using list comprehension.
string = "hello world"
extract_string = [x for x in string]
print(extract_string)


#11)Write a program to create a list containing the length of each word in a sentence.
sentence = "python is easy to learn and understanding"
len_sentence = [len(s) for s in sentence.split()]
print(len_sentence)
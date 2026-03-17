#1)Write a program to filter numbers greater than 50 from a list.
lst = [45,56,18,89,52,90]
greater = [n for n in lst if n > 50]
print(greater)


#2)Write a Python program to extract vowels from a string using list comprehension.
string = "hello world"
vowel = ['a','e','i','o','u']
extract_vowel = [v for v in string if v in vowel]
print(extract_vowel)


#3)Write a program to create a list of numbers that are divisible by both 3 and 5 from 1 to 100.
divisible = [n for n in range(1,101) if n % 3 == 0]
print(divisible)


#4)Write a Python program to convert a list of temperatures in Celsius to Fahrenheit using list comprehension.
temperature = [32,35,33,40,29,45,38,36,42]
fahrenheit = [(temp*9/5) + 32 for temp in temperature]
print(fahrenheit)


#5)Write a program to create a list of the first letter of each word in a sentence.
sentence = "This is a python tutorial"
first_letter = [s[0] for s in sentence.split()]
print(first_letter)


#6)Write a Python program to remove empty strings from a list.
empty_string = ["hello","","world","","python"]
remove_empty_string = [emp for emp in empty_string if emp != ""]
print(remove_empty_string)


#7)Write a program to convert a list of words into lowercase.
words = ["HELLO","WORLD","PYTHON","WELCOME"]
lowercase = [word.lower() for word in words]
print(lowercase)


#8)Write a Python program to create a list of squares of only even numbers.
num = [1,2,3,4,5,6,7,8,9,10]
even_square = [n**2 for n in num if n % 2 == 0]
print(even_square)


#9)Write a program to replace negative numbers with 0 in a list using list comprehension.
negative = [1,-3,2,-6,0,-4,-2]
replace_neg = [0 if n < 0 else n for n in negative]
print(replace_neg)
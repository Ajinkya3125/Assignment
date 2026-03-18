#1)Write a Python program to flatten a nested list using list comprehension.
nested_list = [[1,2,3],[3,4],[5,6,7]]
flatten = [item for sublist in nested_list for item in sublist]
print(flatten)


#2)Write a program to create a list of tuples containing (number, square).
# Example:
# Input → [1,2,3]
# Output → [(1,1), (2,4), (3,9)]
number = [1,2,3]
num_square = [(n,n**2) for n in number]
print(num_square)


#3)Write a Python program to find common elements between two lists using list comprehension.
l1 = [1,2,3,4]
l2 = [2,4,7,8]
common_num = [n for n in l1 if n in l2]
print(common_num)


#4)Write a program to create a list of characters from a string excluding vowels.
string = "hello world"
vowel = "aeiouAEIOU"
exclude_vowel = [v for v in string if v not in vowel]
print(exclude_vowel)


#5)Write a Python program to transpose a matrix using list comprehension.
matrix = [[1,2,3],
          [2,7,6],
          [7,8,0]]
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose_matrix)


#6)Write a program to create a list of numbers that are prime between 1 and 50 using list comprehension.
prime_no = [n for n in range(2,51) if all(n % i != 0 for i in range(2,int(n**0.5)+1))]
print(prime_no)


#7)Write a Python program to remove duplicate elements from a list using list comprehension.
lst = [1,2,3,2,5,3,8,5,7]
dup = []
remove_dup = [dup.append(n) or n for n in lst if n not in dup]
print(remove_dup)


#8)Write a program to create a list of words longer than 5 characters from a sentence.
sentence = "this apple is green and pineapple is yellow"
word = [sen for sen in sentence.split() if len(sen) > 5]
print(word)


#9)Write a Python program to create a list of factorial values from 1 to 10.
import math
factorial = [math.factorial(n) for n in range(1,11)]
print(factorial)


#10)Write a program to create a list of numbers whose square is less than 100.
lst = [1,2,3,4,5,6,7,8,9,10]
square_num = [n for n in lst if n*n < 100]
print(square_num)
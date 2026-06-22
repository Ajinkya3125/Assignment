# Q1)Write a Python program to count the number of odd elements in a list.
lst = [1,2,3,4,5,6,7]   ##first approach
result = len([num for num in lst if num % 2 != 0])
print(result)

lst = [1,2,3,4,5,6,7]   ##second approach
cnt = 0
for l in lst:
    if l % 2 != 0:
        cnt += 1
print(cnt)


#Q2)Write a Python program to find the average of all elements in a tuple.
tup = (10,20,30,40)
total = 0
n = len(tup)
for t in tup:
    total += t
print(total / n)


#Q3)Write a Python program to find all keys whose value is greater than 100.
dic = {"A":50,"B":120,"C":200}   ##first approach
result = []
for key,value in dic.items():
    if value > 100:
        result.append(key)
print(result)

dic = {"A":50,"B":120,"C":200}   ##second approach
result = [key for key, value in dic.items() if value > 100]
print(result)


#Q4)Write a Python program to find the largest element in a set without using max().
set1 = {10,40,20,30}
print(max(set1))

#Q5)Write a Python program to count the number of vowels and consonants in a string.
word = "Python"      ##first approach
vowel = "aeiouAEIOU"
vowel_cnt = 0
consonant_cnt = 0
for ch in word:
    if ch.isalnum:
        if ch in vowel:
            vowel_cnt += 1
        elif ch not in vowel:
            consonant_cnt += 1
print("Number of vowels:",vowel_cnt)
print("Number of consonants:",consonant_cnt)

word = "Python"    #second approach
vowel = "aeiouAEIOU"
vowel_cnt = sum(1 for ch in word if ch in vowel)
consonant_cnt = sum(1 for ch in word if ch.isalpha() and ch not in vowel)
print("Number of vowels:",vowel_cnt)
print("Number of consonants:",consonant_cnt)


#Q6)Write a Python program using list comprehension to create a list of cubes of odd numbers from 1 to 15.
result = [n**3 for n in range(1,16) if n % 2 != 0]
print(result)

#Q7)Write a Python program using a lambda function to find the square of a number.
square = lambda n:n*n
print(square(6))

#Q8)Write a Python program using lambda and filter() to extract all even numbers from a list.
lst = [1,2,3,4,5,6,7,8]
filter_list = list(filter(lambda x : x % 2 == 0,lst))
print(filter_list)

#Q9)Write a Python program using lambda and sorted() to sort a list of tuples based on the second element.
lst = [(1,5), (2,3), (3,1), (4,4)]
result = sorted(lst , key = lambda n:n[1])
print(result)


#Q10)Write a Python program to find the word with the maximum length in a sentence.
sentence = "Python programming is very interesting"
print(max(sentence.split(), key=len))


#Q11)Write a Python program using lambda and map() to create a new list containing the squares of all numbers.
lst = [1,2,3,4,5]
square = list(map(lambda x:x*x,lst))
print(square)


#Q12)Write a Python program using lambda and reduce() to find the product of all numbers in a list.
from functools import reduce
lst = [2,3,4,5]
product = reduce(lambda x, y:x * y,lst)
print(product)
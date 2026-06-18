##Q1)Write a Python program to find the average of all elements in a list.
lst = [10, 20, 30, 40]
n = len(lst)
total = 0
for l in lst:
    total += l
print("Average of all list elements:",total/n)

#Q2)Write a Python program to find the index of an element in a tuple.
tup = (10,20,30,40)
print(tup.index(30))

#Q3)Write a Python program to print all keys of a dictionary.
dic = {"name":"ABC","age":21,"city":"Mumbai"}
for k in dic.keys():
    print(f"{k}")
    
#Q4)Write a Python program to add an element to a set.
set1 = {10,20,30}
set1.add(40)
print(set1)

#Q5)Write a Python program to reverse a string.
str1 = "Python"   ##first approach
print(str1[::-1])

str1 = "Python"   ##second approach
rev = ""
for ch in str1:
    rev = ch + rev
print(rev)

#Q6)Write a Python program to find common elements between two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]
result = []         ##first approach
for l1 in list1:
    if l1 in list2:
        result.append(l1)
print(result)

list1 = [1,2,3,4]     ##second approach
list2 = [3,4,5,6]
s = set(list2)
result = [x for x in list1 if x in s]
print(result)

#Q7)Write a Python program using list comprehension to create a list of squares of numbers from 1 to 15 that are divisible by 3.
square = [n*n for n in range(1,16) if n % 3==0]
print(square)

#Q8)Write a Python program to count the frequency of each character in a string using a dictionary.
str1 = "banana"
freq = {}
for s in str1:
    freq[s] = freq.get(s,0) + 1
print(freq)

#Q9)Write a Python program to find the symmetric difference of two sets.
A = {1,2,3,4}
B = {3,4,5,6}
print(A.symmetric_difference(B))

#Q10)Write a Python program to check whether two strings are anagrams.
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
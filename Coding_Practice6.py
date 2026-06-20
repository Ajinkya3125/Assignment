#Q1)Write a Python program to find the sum of all elements in a list.
lst = [5, 10, 15, 20]
total = 0
for l in lst:
    total += l
print(total)

#Q2)Write a Python program to check whether an element exists in a tuple.
tup = (10, 20, 30, 40)
num = 30
if num in tup:
    print("Element exists")
else:
    print("Element does not exists")
    
#Q3)Write a Python program to find the number of key-value pairs in a dictionary.
dic = {"name":"ABC","age":21,"city":"Pune"}
cnt = 0
for key, value in dic.items():
    cnt += 1
print(cnt)

#Q4)Write a Python program to remove an element from a set.
set1 = {10,20,30,40}
set1.remove(20)
print(set1)

#Q5)Write a Python program to count the number of characters in a string without using len().
str1 = "Python"
cnt = 0
for s in str1:
    cnt += 1
print(cnt)

#Q6)Write a Python program to find the smallest and largest element in a list without using min() or max().
lst = [12, 45, 7, 89, 23]
small = lst[0]
large = lst[0]
for l in lst:
    if l < small:
        small = l
        
    if l > large:
        large = l
    
print("Smallest element=",small)
print("Largest element=",large)

#Q7)Write a Python program using list comprehension to create a list of vowels from a string.
str1 = "education"
vowel = "aeiouAEIOU"
result = [v for v in str1 if v in vowel]
print(result)

#Q8)Write a Python program to merge two dictionaries.
dict1 = {"a":1, "b":2}
dict2 = {"c":3, "d":4}
print(dict1 | dict2)

print({**dict1, **dict2})

dict1.update(dict2)
print(dict1)

#Q9)Write a Python program to check whether two sets are disjoint.
A = {1,2}
B = {3,4}
print(A.isdisjoint(B))

#Q10)Write a Python program to find the longest word in a sentence.
sentence = "The Python programming language"  ##first approach
longest = ""
for s in sentence.split():
    if len(s) > len(longest):
        longest = s
print("Longest word : ",longest)

sentence = "The Python programming language"  ##second approach
longest = max(sentence.split(),key=len)
print("Longest word : ",longest)
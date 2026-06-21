#Q1)Write a Python program to find the product of all elements in a list.
lst = [2,3,4]
prod = 1
for l in lst:
    prod *= l
print("Product of all elements in the list:",prod)


#Q2)Write a Python program to reverse a tuple.
tup = (1,2,3,4,5)
print(tup[::-1])


#Q3)Write a Python program to remove a key from a dictionary.
dic = {"name":"ABC","age":21,"city":"Pune"}
del dic["city"]
print(dic)


#Q4)Write a Python program to find the number of elements in a set without using len().
set1 = {10,20,30,40}
cnt = 0
for s in set1:
    cnt += 1
print(cnt)


#Q5)Write a Python program to count the number of digits in a string.
str1 = "abc123xyz45"
cnt = 0
for s in str1:
    if s.isdigit():
        cnt += 1
print("Total number of digits:",cnt)


#Q6)Write a Python program to split a list into two equal halves.
lst = [1,2,3,4,5,6]
mid = len(lst) // 2
a = lst[:mid]
b = lst[mid:]
print("First Half :",a)
print("Second Half :",b)


#Q7)Write a Python program using list comprehension to create a list of the lengths of words in a sentence
sentence = "Python is very easy"
words = sentence.split()
result = [len(word) for word in words]
print(result)


#Q8)Write a Python program to create a new dictionary containing only the items whose values are greater than 50.
dic = {"A":40,"B":70,"C":90,"D":20} ##first approach
new_dic = {}
for key, value in dic.items():
    if value > 50:
        new_dic[key] = value
print(new_dic)


dic = {"A":40,"B":70,"C":90,"D":20}  ##second approach
result = {key : value for key, value in dic.items() if value > 50}
print(result)


#Q9)Write a Python program to remove all common elements from two sets.
A = {1,2,3,4}
B = {3,4,5,6}
common = A & B
A = A - common
B = B - common
print(A)
print(B)


#Q10)Write a Python program to find the character that appears the maximum number of times in a string.
str1 = "mississippi"
freq = {}
for s in str1:
    freq[s] = freq.get(s,0) + 1

max_char = max(freq, key=freq.get)
print("character with maximum frequency :",max_char)


#Q)Extra question
# Write a Python program to find all unique words in a sentence.
sentence = "python is easy and python is powerful"  ##first approach
words = sentence.split()
result = [word for word in words if words.count(word) == 1]
print(result)


sentence = "python is easy and python is powerful"  #second approach
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
result = [word for word in words if freq[word] == 1]
print(result)
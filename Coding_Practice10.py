#Q1)Write a Python program to find the count of positive numbers in a list.
lst = [-2, 5, -1, 8, 10, -3, 3]
cnt = 0
for l in lst:
    if l > 0:
        cnt += 1
print("Total positive numbers in list:",cnt)


#Q2)Write a Python program to find the first occurrence index of an element in a tuple.
tup = (10,20,30,20,40)    ##first approach
element = 20
for i in range(len(tup)):
    if tup[i] == element:
        print("First occurence index:",i)
        break
    
tup = (10,20,30,20,40)    ##second approach
print("First occurence index:",tup.index(20))


#Q3)Write a Python program to create a dictionary from two lists.
keys = ["name", "age", "city"]  #first approach
values = ["ABC", 21, "Pune"]
dic = {}
for k, v in zip(keys, values):
    dic[k] = v
print(dic)

keys = ["name", "age", "city"]   #second approach
values = ["ABC", 21, "Pune"]
dic = dict(zip(keys,values))
print(dic)


#Q4)Write a Python program to remove all elements from a set one by one using a loop.
set1 = {10,20,30}
while set1:
    print("Remove element:",set1.pop())
print("Set after removal:",set1)


#Q5)Write a Python program to find the number of uppercase letters in a string.
str1 = "PyTHon"
cnt = 0
for s in str1:
    if s.isupper():
        cnt += 1
print(cnt)


#Q6)Write a Python program to move all zeros to the end of a list.
lst = [1,0,2,0,3,4,0]
new_lst = []            #first approach
for i in lst:
    if i != 0:
        new_lst.append(i)

for i in lst:
    if i == 0:
        new_lst.append(i)
print(new_lst)

lst = [1,0,2,0,3,4,0]   ##second approach
new_lst = [i for i in lst if i != 0] + [i for i in lst if i == 0]
print(new_lst)


#Q7)Write a Python program using list comprehension to create a list of numbers from 1 to 50 that are divisible by 4.
result = [n for n in range(1,51) if n % 4 == 0]
print(result)


#Q8)Write a Python program using lambda and map() to convert all strings in a list to uppercase.
subject = ["python", "java", "c++"]
result = list(map(lambda x : x.upper(),subject))
print(result)

#Q9)Write a Python program using lambda and filter() to extract all words whose length is greater than 4.
language = ["cat", "python", "java", "programming", "sql"]
result = list(filter(lambda x : len(x) > 4,language))
print(result)


#Q10)Write a Python program to find the least frequent character in a string.
str1 = "programming"
freq = {}
for s in str1:
    freq[s] = freq.get(s,0) + 1
least_char = min(freq, key=freq.get)
print(least_char)


#Q11)Write a Python program using lambda and sorted() to sort a list of dictionaries by the "age" key.
students = [
    {"name":"A", "age":22},
    {"name":"B", "age":19},
    {"name":"C", "age":25}
]
result = sorted(students, key = lambda students : students["age"])
print(result)


#Q12)Write a Python program to find all words that start with a vowel from a sentence.
sentence = "apple banana orange umbrella mango elephant"
words = sentence.split()
empty_lst = []
vowel = "aeiouAEIOU"
for word in words:
    if word[0] in vowel:
        empty_lst.append(word)
print(empty_lst)
#Q1)Write a Python program to find the difference between the largest and smallest element in a list
lst = [10, 25, 5, 40, 15]
small = lst[0]
large = lst[0]
for l in lst:
    if l < small:
        small = l
        
    if l > large:
        large = l
print("Difference between largest and smallest:",large-small)


#Q2)Write a Python program to count the number of even elements in a tuple.
tup = (1,2,3,4,5,6)
cnt = 0
for t in tup:
    if t % 2 == 0:
        cnt += 1
print("Total number of even elements:",cnt)


#Q3)Write a Python program to check whether a value exists in a dictionary.
dic = {"name":"ABC","age":21}
if 21 in dic.values():
    print("Value exists")
else:
    print("Value does not exists")
    

#Q4)Write a Python program to find the sum of all elements in a set.
set1 = {10,20,30,40}
total = 0
for s in set1:
    total += s
print("Sum of all elements in a set:",total)


#Q5)Write a Python program to count the number of spaces in a string.
sentence = "Python is easy to learn"
cnt = 0
for sen in sentence:
    if sen == " ":
        cnt += 1
print(cnt)


#Q6)Write a Python program to rotate a list by one position to the right.
lst = [1,2,3,4,5]
result = [lst[-1]] + lst[:-1]
print(result)


#Q7)Write a Python program using list comprehension to create a list of numbers between 1 and 50 that are divisible by both 2 and 5.
result = [n for n in range(1,51) if n % 2 == 0 and n % 5 == 0]
print(result)


#Q8)Write a Python program to swap keys and values in a dictionary.
dic = {"a":1,"b":2,"c":3}
swapped = {}
for key, value in dic.items():   ##first approach
    swapped[value] = key
print(swapped)

dic = {"a":1,"b":2,"c":3}  ##second approach
swapped = {value:key for key, value in dic.items()}
print(swapped)


#Q9)Write a Python program to find elements that are present in Set A but not in Set B and vice versa.
A = {1,2,3,4}
B = {3,4,5,6}
common = A & B
A = A - common
B = B - common
print(A)
print(B)


#Q10)Write a Python program to count the frequency of each word in a sentence.
sentence = "python is easy and python is powerful"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word,0) + 1
print(freq)
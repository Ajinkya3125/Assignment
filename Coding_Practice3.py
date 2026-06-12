# Q1)Write a Python program to find the largest element in a list.
# Example:
# Input → [10,25,5,40,12]
# Output → 40
lst = [10,25,5,40,12]
print("Maximum number:",max(lst))


#Q2)Write a Python program to find the maximum and minimum element in a tuple.
# Example:
# Input → (4,8,2,9,1)
# Output → Maximum = 9
# Minimum = 1
tup1 = (4,8,2,9,1)
min_num = tup1[0]
max_num = tup1[0]
for t in tup1:
    if t < min_num:
        min_num = t
    
    if t > max_num:
        max_num = t
        
print("Minimum number:",min_num)      
print("Maximum number:",max_num)
    
    
#Q3)Write a Python program to print all keys and values in a dictionary.
#input-{"name":"ABC","age":21}
#output-name : ABC
#age : 21
dic = {"name":"ABC","age":21}
for k,v in dic.items():
    print(f"{k}:{v}")
    
    
#Q4)Write a Python program to find the union of two sets.
# Example:
# Set1 → {1,2,3}
# Set2 → {3,4,5}
# Output → {1,2,3,4,5}
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 | set2)
print(set1.union(set2))


#Q5)Write a Python program to count the number of vowels in a string
# Example:
# Input → "education"
# Output → 5
str1 = "education"
vowel = "aeiouAEIOU"
cnt = 0
for s in str1:
    if s in vowel:
        cnt += 1
print("total number of vowel:",cnt)


#Q6)Write a Python program to reverse a list without using reverse() method.
# Example:
# Input → [1,2,3,4,5]
# Output → [5,4,3,2,1]
lst = [1,2,3,4,5]
print(lst[::-1])


#Q7Write a Python program using list comprehension to create a list of numbers divisible by 3 from 1 to 30.
result = [n for n in range(1,31) if n % 3 == 0]
print(result)


#Q8)Write a Python program to find the sum of all values in a dictionary.
dic = {"a":10,"b":20,"c":30}
sum = 0
for v in dic.values():
    sum += v
print(sum)


#Q9)Write a Python program to check whether one set is a subset of another set.
A = {1,2}
B = {1,2,3,4}
print(A.issubset(B))


#Q10)Write a Python program to remove all spaces from a string.
s = "Python Programming"
print(s.replace(" ", ""))
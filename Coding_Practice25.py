#Part A: zip()
#Q1) Combine Two Lists
names = ["Ajinkya", "Rahul", "Priya"]
marks = [85, 90, 78]
for n,m in zip(names,marks):
    print(f"{n} : {m}")
    
    
#Q2)Create a Dictionary Using zip()
keys = ["name", "age", "city"]
values = ["ABC", 21, "Pune"]
print(dict(zip(keys,values)))


#Q3)Use zip() to create a new list containing the sum of corresponding elements.
A = [10,20,30]
B = [1,2,3]
result = []
for a,b, in zip(A,B):
    result.append(a + b)
print(result)


#Q4)Print Two Lists Together
fruits = ["Apple", "Banana", "Mango"]
prices = [120, 50, 80]
for f,p in zip(fruits,prices):
    print(f"{f} costs {p}")
    

#Part B: enumerate()
#Q5) Print Index and Value
subjects = ["Python", "Java", "C++", "SQL"]
for index,value in enumerate(subjects):
    print(index,value)
    
    
#Q6)Start Index from 1, using the start parameter of enumerate().
subjects = ["Python", "Java", "C++", "SQL"]
for index,value in enumerate(subjects,start=1):
    print(index,value)
    
    
#Q7)Find the Position of an Element and Use enumerate() to print the index of "Green".
colors = ["Red", "Blue", "Green", "Yellow"]
for index,color in enumerate(colors):
    if color == "Green":
        print(f"Green found at index {index}")
        

#Part C: any()
#Q8) Check for Positive Numbers and Use any() to check whether at least one number is positive.
numbers = [-2, -5, 0, 8, -1]
result = any(n > 0 for n in numbers)
print(result)


#Q9)Use any() to check whether the word contains at least one vowel.
word = "sky"
vowels = "aeiouAEIOU"
result = any(w in vowels for w in word)
print(result)


#Part D: all()
#Q10)Use all() to check whether all numbers are positive.
numbers = [2,5,8,10]
result = all(n > 0 for n in numbers)
print(result)


#Q11)Use all() to check whether every word is uppercase.
words = ["PYTHON", "JAVA", "SQL"]
result = all(w.isupper() for w in words)
print(result)


# Part E: sorted()
# Q12) Sort a List in ascending order.
numbers = [25,10,40,5,18]
print(sorted(numbers))


#Q13)Sort the same list in descending order.
numbers = [25,10,40,5,18]
print(sorted(numbers,reverse=True))


#Q14)Q14) Sort a List of Tuples Sort by marks.
students = [("Rahul",75),("Ajinkya",90),("Priya",82)]
result = sorted(students ,key = lambda x:x[1])
print(result)


#Q15) Sort using the length of each word.
words = ["cat", "elephant", "dog", "python"]
result = list(sorted(words, key= lambda x:len(x)))
print(result)


#Part F: reversed()
# Q16) Reverse a List
numbers = [1,2,3,4,5]
rev = list(reversed(numbers))
print(rev)


#Q17) Reverse a String
text = "Python"
result = "".join(reversed(text))
print(result)


#Q18) using zip() to Combine Three Lists
names = ["A","B","C"]
ages = [20,21,22]
cities = ["Pune","Mumbai","Delhi"]
for one,two,three in zip(names,ages,cities):
    print(f"{one} {two} {three}")
    
    
#Q19)Use any() to check whether duplicates exist in the list.
numbers = [1,2,2,3,4,5]
result = any(numbers.count(n) > 1 for n in numbers)
print(result)


#Q20)Sort the dictionary items by values using sorted().
students = {"A":80,"B":95,"C":70}
result = list(sorted(students.items(), key= lambda x:x[1]))
print(result)


#Q21)Use enumerate() to print only the even-indexed elements of a list.
number = [1,2,3,4,5,6]
for index,value in enumerate(number):
    if index % 2 == 0:
        print(value)
        
        
#Q22)Use zip() to multiply corresponding elements of two lists.
A = [1,2,3]
B = [4,5,6]
result = []
for a,b in zip(A,B):
    result.append(a*b)
print(result)


#Q23)Use all() to check whether every element in a list is an integer.
number = [10,20,30,40,50]
result = all(isinstance(num,int) for num in number)
print(result)


#Q24)Use reversed() to check whether a string is a palindrome.
string = "madam"
if string == "".join(reversed(string)):
    print("Palindrome")
else:
    print("Not Palindrome")
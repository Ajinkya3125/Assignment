##1)Write a Python program to create a dictionary of student names and marks.
students = {
    "Ajinkya":90,
    "Gaurav":89,
    "Sachin":80
}
print(students)


##2)Write a program to add a new key-value pair to a dictionary.
students["Dattatray"] = 95 #first approach
print(students)

name = input("Enter the name:") #second approach
marks = int(input("Enter the marks:"))
students[name] = marks
print(students)

students.update({"Soham":85})  #third approach
print(students)


#3)Write a program to delete a key from a dictionary.
fruit = {"name":"Mango", "price":1000}
del fruit["name"]
print(fruit)


#4)Write a program to find the key with the highest value in a dictionary.
student = {'Ajinkya': 90, 'Gaurav': 89, 'Sachin': 80, 'Dattatray': 95}
print("Highest marks:",max(student.values()))  #first approach

highest_student = max(students, key=students.get)  #second approach
print("Student Name:",highest_student)
print("Highest Marks:",student[highest_student])


#5) Write a Python program to count the frequency of characters in a string using a dictionary.
string = "Hello all of you"
freq = {}
for ch in string:
    freq[ch] = freq.get(ch,0) + 1
print(freq)


#6)Write a program to merge two dictionaries.
dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'f':6}
result = {**dict1,**dict2}
print(result)
print(dict1 | dict2)


#7)Write a program to check if a key exists in a dictionary.
dict1 = {"name":"om","age":29}
if "age" in dict1:
    print("yes")
else:
    print("No")


#8)Write a program to print all keys and values in a dictionary.
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for key,value in dict1.items():
    print(f"{key}:{value}")


#9)Write a Python program to sort a dictionary by values.
dict1 = {'a': 5, 'b': 2, 'c': 1, 'd': 4, 'e': 8, 'f': 7}
sorted_dict = dict(sorted(dict1.items(),key=lambda x:x[1]))
print(sorted_dict)


#10)Write a program to find the sum of all values in a dictionary.
dict1 = {'a': 5, 'b': 2, 'c': 1, 'd': 4, 'e': 8, 'f': 7}
sum_dict = sum(dict1.values())
print("Sum of all values in the dictionary:",sum_dict)

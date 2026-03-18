#1)# Write a Python program to convert a list of tuples into a list of their second elements.
lst_tup = [(1,10),(2,20),(3,30),(4,40)]
lst = [t[1] for t in lst_tup]
print(lst)


#2)Write a program to create a list of ASCII values of characters in a string.
string = "hello world"
ascii_value = [ord(s) for s in string]
print(ascii_value)


#3)Write a Python program to create a list of digits from a string containing numbers.
string = "12345"
string_num = [int(n) for n in string]
print(string_num)


#4)Write a program to create a list of reversed strings from a list of words.
string = ["hello","world","apple","orange"]
rev_string = [s[::-1] for s in string]
print(rev_string)


#5)Write a Python program to remove spaces from a string using list comprehension.
string = "he ll o worl d"
remove_space = [s for s in string if s != " "]
print(remove_space)


#6)Write a program to create a multiplication table of 5 using list comprehension.
n=5
five_table = [n*i for i in range(1,11)]
print(five_table)


#7)Write a program to create a list of boolean values checking whether numbers are even.
number = [1,4,8,3,2,9,6,5]
boolean_value = [n % 2 == 0 for n in number]
print(boolean_value)


#8)Write a Python program to create a list of numbers divisible by 7 from 1 to 100.
divisible = [i for i in range(1,101) if i % 7 == 0]
print(divisible)


#9)Write a Python program to create a list of unique elements from a list using list comprehension.
lst = [1,2,2,3,4,8,6,4]
seen = []
unique_element = [seen.append(n) or n for n in lst if n not in seen]
print(unique_element)


#10)Write a program to create a list of the sum of pairs from two lists using list comprehension.
# Example:
list1 = [1,2,3]
list2 = [4,5,6]
# Output → [5,7,9]
sum_list = [l1+l2 for l1, l2 in zip(list1, list2)]
print(sum_list)
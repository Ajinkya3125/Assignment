#1)Write a Python program to iterate through all key-value pairs in a dictionary.
dict1 = {"name":"Ajinkya","age":21,"class":"Msc(Computer Science)"}
for key,value in dict1.items():
    print(f"{key}:{value}")

#2)Write a program to merge two dictionaries into one.
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"d":4,"e":5,"f":6}
print(dict1 | dict2)
print({**dict1, **dict2})


#3)Write a Python program to find the sum of all values in a dictionary.
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
sum_value = sum(d1.values())
print(sum_value)


#4)Write a program to find the maximum value in a dictionary.
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}  #first approach
max_value = max(d1.values())
print("Maximum value:",max_value)

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}  #second approach
max_value = 0
for value in d1.values():
    if value > max_value:
        max_value = value
print("Maximum value:",max_value)


#5) Write a Python program to find the minimum value in a dictionary.
d1 = {'a': 3, 'b': 2, 'c': 1, 'd': 4, 'e': 5, 'f': 9}  #first approach
min_value = list(d1.values())[0]
for value in d1.values():
    if value < min_value:
        min_value = value
print("Minimum value:",min_value)


d1 = {'a': 3, 'b': 2, 'c': 1, 'd': 4, 'e': 5, 'f': 9}  #second approach
print("Minimum value:",min(d1.values()))


#6) Write a program to sort a dictionary by keys.
dict1 = {"orange":20,"apple":30,"banana":10,"cherry":42}
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)


#7) Write a program to sort a dictionary by values.
dict1 = {"orange":20,"apple":30,"banana":10,"cherry":42}
sorted_dict = dict(sorted(dict1.items(),key=lambda x:x[1]))
print(sorted_dict)


#8)Write a Python program to invert a dictionary (swap keys and values).
dict1 = {"orange":20,"apple":30,"banana":10,"cherry":42}  #first approach
for key,value in dict1.items():
    print(f"{value}:{key}")

dict1 = {"orange":20,"apple":30,"banana":10,"cherry":42}  #second approach
inv_dict = {}
for k,v in dict1.items():
    inv_dict[v] = k
print(inv_dict)

dict1 = {"orange":20,"apple":30,"banana":10,"cherry":42}  #third approach
inv_dict = {v:k for k,v in dict1.items()}
print(inv_dict)


#9) Write a program to copy one dictionary into another.
d1 = {'a': 1, 'b': 2, 'c': 3} #first approach
d2 = d1
print(d2)

d1 = {'a': 1, 'b': 2, 'c': 3}  #second approach
d2 = d1.copy()
print(d2)


#10)Write a Python program to create a dictionary from two lists (keys and values).
keys = ['a', 'b', 'c', 'd']   #first approach
values = [1, 2, 3, 4]
dict1 = dict(zip(keys,values))
print(dict1)


keys = ['a', 'b', 'c', 'd']   #second approach
values = [1, 2, 3, 4]
dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)
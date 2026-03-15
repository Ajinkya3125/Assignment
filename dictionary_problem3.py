#1)Write a Python program to count the frequency of words in a sentence.
sentence = "this is a builing and This iS a dog."
words = sentence.lower().split()
print(words)
freq = {}
for word in words:
    if word.lower():
        freq[word] = freq.get(word,0) + 1
print(freq)


#2)Write a program to find the key with the highest value in a dictionary.
fruit = {"apple":200,"banana":310,"papaya":120,"strawberry":360}
high_key = max(fruit,key=fruit.get)
high_value = fruit[high_key]
print("High key:",high_key)
print("High value:",high_value)


#3)Write a Python program to remove duplicate values from a dictionary.
fruit = {"apple":20,"banana":30,"papaya":20,"strawberry":3}
dup = {}
for k,v in fruit.items():
    if v not in dup.values():
        dup[k] = v
print(dup)


#4)Write a program to check if two dictionaries are equal.
d1 = {"a":1,"b":2,"c":3}
d2 = {"a":1,"b":2,"c":3}
if d1 == d2:
    print("equal")
else:
    print("Not equal")


#5)Write a Python program to create a nested dictionary.
student = {
    "name":"Ajinkya",
    "age":21,
    "subject":{
        "Marathi":82,
        "Hindi":87,
        "English":93
    }
}
print(student)

#6)Write a program to access elements from a nested dictionary.
print(student["subject"]["Marathi"])

#7)Write a Python program to flatten a nested dictionary.
d = {"a":1,"b":{"x":2,"y":3},"c":4}
flat = {}
for k,v in d.items():
    if type(v) == dict:
        for i,j in v.items():
            flat[k+"_"+i] = j
    else:
        flat[k] = v
print(flat)

#8)Write a program to find all keys that have the same value.
fruit = {"apple":20,"banana":30,"papaya":20,"strawberry":3}
same_key = {}
for k1, v1 in fruit.items():
    cnt = 0
    for v2 in fruit.values():
        if v1 == v2:
            cnt += 1
        if cnt > 1:
            same_key[k1] = v1
print(same_key)

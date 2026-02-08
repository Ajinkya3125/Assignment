##Count frequency of characters in a string
string = "programming"
dic = {}
for d in string:
    dic[d] = dic.get(d,0) + 1
print(dic)


##Find the first non-repeating character
string = "aasbbcdd"
dic = {}
for d in string:
    dic[d] = dic.get(d,0) + 1
    
for d in string:
    if dic[d] == 1:
        print(d)
        break
    
    
##Find the key with maximum value
dic = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
dic_max = max(dic,key=dic.get)
print(dic_max)


##Merge two dictionaries (values added if key exists)
dict1 = {'p': 1, 'r': 2, 'o': 1}
dict2 = {'o': 2, 'a': 1, 'm': 2}
for k,v in dict2.items():
    dict1[k] = dict1.get(k,0) + v
print(dict1)


##Check if two strings are anagrams
str1 = "book"
str2 = "koob"

dict1 = {}
dict2 = {}
for i in str1:
    dict1[i] = dict1.get(i,0) + 1
    
for j in str2:
    dict2[j] = dict2.get(j,0) + 1
    
print(dict1 == dict2)



##Remove duplicate values from dictionary
dict1 = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'k': 1, 'm': 2}
result = {}
for k,v in dict1.items():
    if v not in result.values():
        result[k] = v
print(result)



##invert a dictionary
dict1 = {'a': 1, 'b': 2, 'd': 3}
d = {}
for k,v in dict1.items():
    d[v] = k
print(d)


##Group elements with same values
lst = ['apple', 'ant', 'bat', 'ball', 'cat', 'dog','and']
result = {}
for word in lst:
    key = word[0]
    result.setdefault(key,[]).append(word)
print(result)


##Find most frequent element in a list
lst = [1, 3, 2, 1, 4, 1, 3, 3]
freq = {}
for f in lst:
    freq[f] = freq.get(f,0) + 1

print(max(freq,key=freq.get))



##Sort dictionary by values
d = {"a": 3, "c": 1, "b": 2}
sorted_d = dict(sorted(d.items(),key=lambda x:x[0]))
print(sorted_d)
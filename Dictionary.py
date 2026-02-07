#Count frequency of elements
lst = [1,2,2,3,4,3,3,5,6]
dt = {}
for d in lst:
    dt[d] = dt.get(d,0) + 1
print(dt)


#Find key with maximum value
dict1 = {'a':10,'b':20,'c':50}
max_key = max(dict1,key=dict1.get)
print(max_key)


#Merge two dictionaries
dict1 = {'a':10,'b':20}
dict2 = {'c':40,'d':80}
merge_dict = {**dict1,**dict2}
print(merge_dict)


#remove the duplicates
dict1 = {'a': 10, 'b': 10, 'c': 40, 'd': 80}
d = {}
for key,value in dict1.items():
    if value not in d.values():
        d[key] = value
print(d)


#Invert a dictionary
dict1 = {'a': 10, 'b': 20, 'c': 40, 'd': 80}
inv = {}
for k,v in dict1.items():
    inv[v] = k
print(inv)
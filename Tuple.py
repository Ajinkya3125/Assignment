##Find Maximum and Minimum in a Tuple
tup1 = (1,4,8,9)
print("Min number:",min(tup1))
print("Max number:",max(tup1))


##Count Frequency of Elements in a Tuple
tup1 = (1,2,2,3,3,3,4,4)
freq = {}
for t in tup1:
    freq[t] = freq.get(t,0) + 1
print(freq)


##Remove Duplicates from Tuple (Preserve Order)
tup1 = (1,2,2,3,3,3,4,4)
result = []
seen = set()
for t in tup1:
    if t not in result:
        seen.add(t)
        result.append(t)
print(tuple(result))


##Reverse a Tuple
t = (1,2,3,4)
print(t[::-1])


##Check if Element Exists in Tuple
t = (1,3,5,7,9)
print(3 in t)


##Convert Tuple of Tuples into Dictionary
t = (('a', 1), ('b', 2), ('c', 3))
d = dict(t)
print(d)


##Swap Two Tuples
t1 = (1,2,3)
t2 = (2,4,6)
t1,t2 = t2,t1
print(t1,t2)


##Sort Tuple of Tuples by Second Element
t = ((1, 3), (4, 1), (2, 2))
sorted_tup = tuple(sorted(t,key=lambda x:x[1]))
print(sorted_tup)


##Sum of tuple elements
t = (1,2,3,4,5)
print(sum(t))


##Flatten a Nested Tuple
tup = ((1,2),(3,4),(5,))
flat = []
for t in tup:
    for f in t:
        flat.append(f)
print(tuple(flat))


##Pair Elements from Two Tuples
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
result = tuple(zip(t1,t2))
print(result)


##Find Index of Element in Tuple
tup1 = (10,20,30,40,50)
print(tup1.index(30))
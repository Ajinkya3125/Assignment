##Tuple
##1)Write a Python program to create a tuple and print its elements.
tup = (1,2,3,4,5)
print(tup)


##2)Write a program to find the length of a tuple without using len().
tup = (1,2,3,4,8,9,5,6)
cnt = 0
for t in tup:
    cnt = cnt + 1
print(cnt)


##3)Write a Python program to convert a tuple into a list.
tup = (1,2,3,4,5)
lst = list(tup)
print(lst)


##4)Write a program to count how many times an element appears in a tuple.
tup = (1,2,2,3,4,2,5,6)
key = 2
count = 0
for t in tup:
    if t == key:
        count += 1
print("Count:",count)


##5)Write a Python program to find the maximum and minimum value in a tuple.
tup = (1,2,3,4,5,8)
min = tup[0]
max = tup[0]
for t in tup:
    if t < min:
        min = t
    if t > max:
        max = t
print("Minimum number:",min)
print("Maximum number:",max)


##6)Write a Python program to find the sum of all elements in a tuple.
tup = (1,2,3,4,5,6)
sum = 0
for t in tup:
    sum += t
print(sum)


##7)Write a Python program to find the index of an element in a tuple.
tup = (1,2,3,4,5)
key = 3
for i in tup:
    if tup[i] == key:
        print("index:",i)
        break
    

##8)Write a Python program to unpack tuple elements into variables.
tup = (1,2,3,4,5,6)
a,*b,c = tup
print(a)
print(b)
print(c)


##9)Write a program to swap two tuples.
t1 = (1,2,3)
t2 = (4,5,6)
t1,t2 = t2,t1
print(t1,t2)


#10)Write a Python program to remove duplicate elements from a tuple.
tup = (1,2,2,3,4,4,5)
dup = []
for t in tup:
    if t not in dup:
        dup.append(t)
print(tuple(dup))


#11)Write a program to find the product of all elements in a tuple
tup = (1,2,3,4,5)
prod = 1
for t in tup:
    prod *= t
print(prod)


##12)Write a program to merge two tuples and remove duplicates.
tup1 = (1,2,3,3,4,5)
tup2 = (2,4,5,6,1)
result = tup1 + tup2
empty = []
for r in result:
    if r not in empty:
        empty.append(r)
print(tuple(empty))


##13)Write a Python program to reverse a tuple.
tup = (1,2,3,4,5)
rev = []
for r in tup:
    rev = [r] + rev
print(tuple(rev))


##14)Write a program to convert a tuple of strings into uppercase strings.
tup = ("hello","world","play","cricket")  ##first approach
new_t = []
for t in tup:
    new_t.append(t.upper())
print(tuple(new_t))


tup = ("hello","world","play","cricket")  ##second approach
new_t = tuple(t.upper() for t in tup)
print(new_t)


##15)Write a Python program to count even and odd numbers in a tuple.
tup = (1,2,3,4,5,6,7,8,9)
even = 0
odd = 0
for t in tup:
    if t % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:",even)
print("Odd numbers:",odd)


##16)Write a program to find common elements between two tuples.
tup1 = (1,2,3,4)
tup2 = (2,3,1,7)
common = []
for t1 in tup1:
    if t1 in tup2:
        common.append(t1)
print(tuple(common))
        
        

#17)Write a Python program to create a tuple of squares from 1 to 10.
square = []
for i in range(1,11):
    square.append(i * i)
print(tuple(square))


##18)Write a program to find the frequency of elements in a tuple using a dictionary.
tup = (1,2,2,3,1,5,6,4,4)
freq = {}
for t in tup:
    freq[t] = freq.get(t,0) + 1
print(freq)


##19)Write a Python program to check whether all elements in a tuple are unique.
tup = (1,2,3,3,4,5,6)
if len(tup) == len(set(tup)):
    print("All are unique")
else:
    print("Not unique")
    
    
##20Write a program to find the smallest and largest element in a tuple without using built-in functions.
tup = (2,1,7,5,9)
min = tup[0]
max = tup[0]
for t in tup:
    if t < min:
        min = t
    if t > max:
        max = t
print("Smallest:",min)
print("Largest:",max)
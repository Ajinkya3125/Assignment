#1)Write a Python program to create a set and print its elements.
s = {1,2,3,4,5}
print(s)

#2)Write a program to find the union of two sets.
s1 = {1,2,3,4,5}
s2 = {2,1,6,7,4,9}
print(s1 | s2)


#3)Write a Python program to find the intersection of two sets.
s1 = {1,2,3,4,5}
s2 = {2,1,6,7,4,9}
print(s1 & s2)


#4)Write a program to find the difference between two sets.
s1 = {1,2,3,4,5}
s2 = {2,1,6,7,4,9}
print(s1 - s2)


#5)Write a program to remove duplicate elements from a list using a set.
lst = [1,2,2,3,4,4,5,5]
s = set(lst)
print(list(s))


#6)Write a program to print all elements of a set using a loop.
s = {1,2,3,4,5}
for i in s:
    print(i)
    
#7)Write a Python program to add an element to a set.
s = {1,2,3,4,5}
s = list(s)
s[0] = 10
print(set(s))


#8)Write a program to find the symmetric difference between two sets
s1 = {1,2,3,4,5}
s2 = {2,1,6,7,4,9}
print(s2.symmetric_difference(s1))  #first approach
print(s1 ^ s2)   #second approach
print((s1 - s2) | (s2 - s1))   #third approach


#9)Write a Python program to check if one set is a subset of another set.
s1 = {1,2,3}
s2 = {2,1,6,3,4,9}
print(s1.issubset(s2))
print(s1 <= s2)


#10)Write a program to check if one set is a superset of another set.
s1 = {1,2,3}
s2 = {2,1,6,3,4,9}
print(s1.issuperset(s2))
print(s1 >= s2)


#11)Write a Python program to check if two sets are disjoint.
s1 = {1,3,5,7}
s2 = {2,4,6,8}
print(s1.isdisjoint(s2))  #first approach

if s1.intersection(s2):  #second approach
    print("Not disjoint")
else:
    print("Disjoint")


#12)Write a program to remove common elements from two sets.
s1 = {2, 3, 4, 5, 10}
s2 = {3, 5, 6, 7, 9}
common = s1.intersection(s2)   #first approach
s1 = s1 - common
s2 = s2 - common
print("Set1:",s1)
print("Set2:",s2)


s1 -= s1 & s2   #second approach
s2 -= s1 & s2
print(s1, s2)


#13)# Write a Python program to find elements present in only one of the two sets.
s1 = {2, 3, 4, 5, 10}
s2 = {3, 5, 6, 7, 9}
print(s1.symmetric_difference(s2))    #first approach
print(s1 ^ s2)   #second approach

#14)Write a Python program to convert a list into a set.
lst = [1,2,3,4,5]
print(set(lst))


#15)Write a program to convert a string into a set of characters.
string = "Hello world"
lst = []
for s in string:
    lst.append(s)
print(set(lst))
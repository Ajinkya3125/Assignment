##Remove Duplicates from List
lst = [1,2,2,3,3,4]
print(list(set(lst)))


##Find Common Elements Between Two Sets
set1 = {1,2,3,4}
set2 = {2,4,6,8}
result = set1 & set2
print(result)


##Union of Two Sets
set1 = {1,2,3,4}
set2 = {2,4,6,8}
result = set1 | set2
print(result)


##Difference Between Two Sets
set1 = {1,2,3,4}
set2 = {2,4,6,8}
result = set1 - set2
print(result)


##Symmetric Difference
set1 = {1,2,3,4}
set2 = {2,4,6,8}
result = set1 ^ set2
print(result)


##Check Subset and Superset
set1 = {1,2,3,4}
set2 = {2,4,6,8}
print(set1.issubset(set2))
print(set2.issuperset(set1))


##Count Unique Characters in String
str1 = "programming"
print(len(set(str1)))


##Find Missing Number Using Set
nums = [1, 2, 4, 5]
print(set(range(1,6)) - set(nums))


#Check if Two Lists Have Common Elements
set1 = {1,2,3,4}
set2 = {2,4,6,8}
print(bool(set(set1) & set(set2)))


##Remove Common Elements from Set
set1 = {1,2,3}
set2 = {2,3}
set1 -= set2
print(set1)


##set methods
s = {1,2,3}
s.add(4)
print(s)
s.remove(3)
print(s)
s.discard(4)
print(s)
x = s.pop()
print(x)
print(s)
s.clear()
print(s)


##Check if a list contains duplicate elements
s = [1,2,3,4,5]
if len(s) != len(set(s)):
    print("Duplicate present")
else:
    print("Duplicate not present")
    

##Check if two lists have at least one common element
a = {1,2,3}
b = {2,4,6}
if a & b:
    print("common element found")
else:
    print("Not found")
    
    
##Find all unique vowels in a string
s = "basic programming"
vowel = set("aeiou")
result = set(s.lower()) & vowel
print(result)


##Count unique words in a sentence
sentence = "python is easy and python is powerful"
words = sentence.split()
print(len(set(words)))


##Check if a string is Pangram
import string
s = "the quick brown fox jumps over the lazy dog"
alphabet = set(string.ascii_lowercase)
print(set(s.lower()) >= alphabet)


##Find missing numbers from 1 to N
lst = [1,2,4,6]
n = 6
missing = set(range(1,n+1)) - set(lst)
print(missing)


##Find duplicate elements using set (without extra list)
lst = [1, 2, 3, 2, 4, 3]
seen = set()
duplicates = set()
for x in lst:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print(duplicates)


##Check if two strings are anagrams (using set logic)
s1 = "listen"
s2 = "silent"
print(set(s1) == set(s2))



##Find distinct elements in every row of a matrix
matrix = [
    [1, 2, 2],
    [3, 3, 4],
    [5, 6, 6]
]
result = [set(row) for row in matrix]
print(result)


##Remove common elements from two sets
a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)
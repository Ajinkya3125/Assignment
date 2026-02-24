lst = [3,1,2]
lst.sort()#using sort()
print(lst)


a = [3,1,2]##using sorted()
b = sorted(a)
print(a)
print(b)


##shallow copy
import copy
a = [[1,2],[3,4]]
b = copy.copy(a)
b[0][0] = 100
print(a)


##deep copy
import copy
a = [[1,2],[3,4]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a)


##removing the duplicates
a = [1, 2, 2, 3, 4, 4]
a = list(set(a))##first approach
print(a)


result = []##second approach
for b in a:
    if b not in result:
        result.append(b)
print(result)


a = list(dict.fromkeys(a))##third approach
print(a)


##flatten array/list
matrix = [[1, 2], [3, 4], [5, 6]]##first approach
result = []
for row in matrix:
    for num in row:
        result.append(num)
print(result)


##using list comprehension
result = [num for row in matrix for num in row]##second approach
print(result)
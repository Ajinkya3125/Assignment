##Q1)append one list to other
a = [1,2,3]
b = a
b.append(4)
print(a)


##Q2)Sum of all elements in a list
list1 = [1,2,3,4,5]
sum = 0
for n in list1:
    sum += n
print(sum)


##Q3)Find the largest element in a list
list1 = [1,2,3,4,5]
largest = list1[0]
for num in list1:
    if num > largest:
        largest = num
print(largest)


##Q4)Find the smallest element in a list
list1 = [4,5,2,6,1]
smallest = list1[0]
for num in list1:
    if num < smallest:
        smallest = num
print(smallest)


##Q5)Reverse a list (without using reverse())
##method 1
list1 = [1,2,3,4,5]
rev = []
for r in list1:
    rev.append(r)
print(rev[::-1])

##method 2
lst = [1, 2, 3, 4, 5]
rev = []
for item in lst:
    rev.insert(0, item)
print(rev)


##Q6)Remove duplicate elements from a list
list1 = [1,2,2,3,4,4,5,5]
res = []
for num in list1:
    if num not in res:
        res.append(num)
print(res)


##Q7)Check if an element exists in a list
list1 = [1,6,23,78,3,4,2]
key = int(input("Enter the key:"))
found = False
for num in list1:
    if num == key:
        found = True
        break
print(found)


# ##Q8)Count frequency of an element
list1 = [1,6,6,3,3,8,2,3]
key = int(input("Enter the number:"))
cnt = 0
for num in list1:
    if num == key:
        cnt += 1
print(cnt)


##Q9)Merge two lists
##method 1
list1 = [1,2,3]
list2 = [4,5,6]
merged = []
for num in list1:
    merged.append(num)
for num in list2:
    merged.append(num)
print(merged)

##method 2
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2)


##Q10)Sort a list (Ascending order)
lst = [2,1,6,4,9,10]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)


##Q11)Separate even and odd numbers
lst = [1,2,3,4,5,6,7,8]
even = []
odd = []
for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    
print("Even numbers list:",even)
print("Odd numbers list:",odd)


##Q12)Find common elements in two lists
list1 = [1,2,3,4,5]
list2 = [9,2,1,4,8,]

res = []
for num in list1:
    if num in list2 and num not in res:
        res.append(num)
print(res)


##Q13)Flatten a nested list
lst = [[1,2],[2,3],[4,5],[6,7]]
flat = []
for sublist in lst:
    for num in sublist:
        flat.append(num)
print(flat)
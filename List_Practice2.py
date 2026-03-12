##1)Write a Python program to find the largest and smallest element in a list.
def min_max(lst):
    min = lst[0]
    max = lst[0]
    for l in lst:
        if l < min:
            min = l
        if l > max:
            max = l
    print("Minimum number:",min)
    print("Maximum number:",max)
min_max([1,2,3,4,5])


##2)Write a program to remove duplicate elements from a list.
def remove_duplicate(lst):
    empty = []
    for l in lst:
        if l not in empty:
            empty.append(l)
    print("After removing duplicates:",empty)
remove_duplicate([1,2,2,3,3,4,5])


##3)Write a program to reverse a list without using the reverse() method.
def reverse_lst(lst):   #first approach
    rev = []
    for ch in lst:
        rev.insert(0,ch)
    print("Reverse a list:",rev)
reverse_lst([1,2,3,4,5])

def reverse_lst(lst):    #second approach
    rev = []
    for ch in lst:
        rev = [ch] + rev
    print("Reverse a list:",rev)
reverse_lst([1,2,3,4,5])


##4)Write a program to find the second largest number in a list.
def second_largest(lst):
    first = second = float('-inf')   #first approach
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    print("Second Largest:", second)
second_largest([1,2,3,4,5])


def second_largest(lst):   ##second approach
    lst.sort()
    print("second largest:",lst[-2])
second_largest([1,2,3,4,5])


##5)Write a Python program to count how many times a specific element appears in a list.
def count_num(lst):
    cnt = 0
    key = 3
    for i in lst:
        if i == key:
            cnt += 1
    print(f"element {key} appears in {cnt} times")
count_num([1,2,3,4,3,5,3])



##6)Write a program to merge two lists into one list.
def merge_list(l1,l2):
    result = l1 + l2
    print(result)
merge_list([1,2,3],[4,5,6])


##7)Write a program to find common elements between two lists.
def common_element(l1,l2):  #first approach
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    print(common)
common_element([1,2,3,4],[3,4,1,6])


def common_element(l1,l2):  #secod approach
    common = list(set(l1) & set(l2))
    print(common)
common_element([1,2,3,4],[3,4,1,6])


def common_element(l1,l2):   #third approach
    common = [x for x in l1 if x in l2]
    print(common)
common_element([1,2,3,4],[3,4,1,6])


#8)Write a Python program to remove all even numbers from a list.
def remove_even(lst):
    odd = []
    for e in lst:
        if e % 2 != 0:
            odd.append(e)
    print(odd)
remove_even([1,2,3,4,5,6])


##9)Write a program to sort a list without using the sort() method.
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
sort_list([1,5,2,8,4])


##10)Write a program to split a list into two equal halves.
def list_split(lst):   #first approach
    mid = len(lst) // 2
    first_split = lst[:mid]
    second_split = lst[mid:]
    
    print("First split list:",first_split)
    print("Second split list:",second_split)
list_split([1,2,3,4,5,6])


def list_split(lst):
    mid = len(lst) // 2   #second approach
    first_split = []
    second_split = []
    
    for i in range(len(lst)):
        if i < mid:
            first_split.append(lst[i])
        else:
            second_split.append(lst[i])
    print("First split list:",first_split)
    print("Second split list:",second_split)
list_split([1,2,3,4,5,6])
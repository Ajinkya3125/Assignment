s = {1,2,3,3,4,4,5,6}
s.add(7)
print(s)

##union of two sets
s1 = {1,2,3,5}
s2 = {2,3,4,7,8}
print(s1 | s2)##first approach
print(s1.union(s2))##second approach

##intersection of two sets
s1 = {1,2,3,5}
s2 = {2,3,4,7,8}
print(s1 & s2)##first approach
print(s1.intersection(s2))##second approach

##difference of the two sets
s1 = {1,2,3,5}
s2 = {2,3,4,7,8}
print(s1 - s2)##first approach
print(s1.difference(s2))##second approach

##symmetric difference of the two sets
s1 = {1,2,3,5}
s2 = {2,3,4,7,8}
print(s1 ^ s2)##first approach
print(s1.symmetric_difference(s2))##second approach

##remove the duplicates in the list
nums = [1, 2, 2, 3, 4, 4]
remove_nums = list(set(nums))##first approach
print(remove_nums)

nums = [1, 2, 2, 3, 4, 4]
remove_nums = list(dict.fromkeys(nums))##second approach
print(remove_nums)

nums = [1, 2, 2, 3, 4, 4]
lst = []
seen = set()##third approach
for num in nums:
    if num not in seen:
        seen.add(num)
        lst.append(num)
print(lst)
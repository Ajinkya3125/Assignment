# Q1. Flatten a Nested List (one level)
# Write a function flatten(nested_list) that flattens a list of lists into a single list (only one level deep).
def flatten(nested_list):
    result = []
    for lst in nested_list:
        for l in lst:
            result.append(l)
    return result
print(flatten([[1, 2], [3, 4], [5]]))


#Q2. Valid Parentheses
# Write a function is_valid_parentheses(s) that checks whether a string of brackets (){}[] is balanced and properly nested.
def is_valid_parentheses(s):
    stack = []
    pairs = {'}' : '{', ')' : '(', ']' : '['}
    for ch in s:
        if ch in '{([':
            stack.append(ch)
        elif ch in '})]':
            if not stack and stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
print(is_valid_parentheses("{[()()]}"))



#Q3. Merge Two Sorted Lists
# Write a function merge_sorted(lst1, lst2) that merges two sorted lists into a single sorted list, without using sorted() or .sort().
def merge_sorted(lst1, lst2):
    result = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    result.extend(lst1[i:])
    result.extend(lst2[j:])
    
    return result
print(merge_sorted([1,4,5],[2,3,6]))
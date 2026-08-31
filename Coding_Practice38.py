#Q1. Find the Sum of All Elements in a List
def sum_list(nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum_list([1,2,3,4,5]))


#Q2. Find the Largest Element in a List
def find_max(nums):
    max_num = 0
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num
print(find_max([1,8,3,9,5,6]))


#Q3. Count Occurrences of an Element in a List
def count_occurences(nums, target):
    cnt = 0
    for i in nums:
        if i == target:
            cnt += 1
    return cnt
print(count_occurences([1,2,3,2,4,2,5],2))


#Q4. Check if a String Contains Only Digits
def is_numeric_string(s):
    if s.isdigit():
        return True
    else:
        return False
print(is_numeric_string("12345"))
print(is_numeric_string("122ac"))


#Q5. Find the Average of a List
def find_average(nums):
    n = len(nums)
    total = 0
    for i in nums:
        total += i
    return total / n
print(find_average([1,2,3,4,8]))


#Q6. Merge Two Lists
def merge_lists(list1, list2):
    return list1 + list2
print(merge_lists([1,2,3],[4,5,6]))


#Q7. Count the Number of Words in a String
def count_words(s):
    cnt = 0
    words = s.split()
    for word in words:
        cnt += 1
    return cnt
print(count_words("Python is a great programming language"))


#Q8. Find the Index of an Element in a List
def find_index(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
print(find_index([1,2,3,4,5],4))


#Q9. Check if a String Starts and Ends with the Same Character
def same_start_end(s):
    if s[0] == s[-1]:
        return True
    else:
        return False
print(same_start_end("hello"))


#Q10. Convert a String to Uppercase and Lowercase
def convert_case(s):
    upper_result = ""
    lower_result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            upper_result += chr(ord(ch)-32)
            lower_result += ch
        elif 'A' <= ch <= 'Z':
            upper_result += ch
            lower_result += chr(ord(ch)+32)
        else:
            upper_result += 1
            lower_result += 1
    return (upper_result, lower_result)
print(convert_case("Hello"))
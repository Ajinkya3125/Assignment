# Q1. Factorial of a Number
# Write a function factorial(n) that returns the factorial of a non-negative integer n (without using math.factorial).
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(5))


#Q2. Reverse Words in a Sentence
# Write a function reverse_words(sentence) that reverses the order of words in a sentence (not the letters within each word).
def reverse_words(sentence):
    words = sentence.split()
    reversed_word = words[::-1]
    return " ".join(reversed_word)
print(reverse_words("I love Python programming"))


#Q3. Count Occurrences of an Element
# Write a function count_occurrences(lst, target) that returns how many times target appears in lst, without using the built-in .count() method.
def count_occurrences(lst, target):
    cnt = 0
    for l in lst:
        if l == target:
            cnt += 1
    return cnt
print(count_occurrences([1, 2, 2, 3, 2, 4, 2],2))


#Q4. Check Even or Odd List
#Write a function count_even_odd(lst) that returns a tuple (even_count, odd_count) for a list of integers.
def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    for l in lst:
        if l % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
print(count_even_odd([1, 2, 3, 4, 5, 6]))
    
#Q5. Remove Duplicates from a List
# Write a function remove_duplicates(lst) that returns a new list with duplicates removed, preserving the original order.
def remove_duplicates(lst):
    result = []
    for l in lst:
        if l not in result:
            result.append(l)
    return result
print(remove_duplicates([4, 5, 4, 6, 5, 7]))

#Q6. Swap Case
# Write a function swap_case(s) that converts all uppercase letters to lowercase and vice versa, leaving non-alphabetic characters unchanged. Do not use Python's built-in .swapcase().
def swap_case(s):
    result = []
    for ch in s:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch)
    return "".join(result)
print(swap_case("Hello World 123"))

#Q7. Longest Word in a Sentence
# Write a function longest_word(sentence) that returns the longest word in a sentence. If there's a tie, return the first one encountered.
def longest_word(sentence):
    words = sentence.split()
    long_word = max(words)
    return long_word
print(longest_word("The quick brown fox jumps"))


#Q8. Binary Search
#Write a function binary_search(lst, target) that returns the index of target in a sorted list using binary search (not linear search). Return -1 if not found.
def binary_search(lst, target):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search([1, 3, 5, 7, 9, 11],7))


# Q9. Multiplication Table
#Write a function multiplication_table(n) that returns a list of strings representing the multiplication table of n from 1 to 10.
def multiplication_table(n):
    table = []
    for i in range(1,11):
        table.append(f"{n} x {i} = {n*i}")
    return table
print(multiplication_table(5))


#Q10. Find Missing Number
# Write a function find_missing(lst) that takes a list containing n-1 distinct numbers from the range 1 to n, and returns the missing number.
def find_missing(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum
print(find_missing([1,2,3,5,6]))
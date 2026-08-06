# Question 1 — Basics
# Write a function is_palindrome(s) that returns True if a string reads the same forwards and backwards (ignoring case and spaces), and False otherwise.
def is_palindrome(s):
    word = s.replace(" ", "").lower()
    return word == word[::-1]
print(is_palindrome("Race car"))


# Question 2 — Dictionaries
# Write a function word_frequency(text) that returns a dictionary mapping each word (lowercase) to how many times it appears in the input string.
def word_frequency(text):
    freq = {}
    for ch in text.split():
        freq[ch] = freq.get(ch,0) + 1
    return freq
print(word_frequency("the cat sat on the mat"))


# Question 3 — Recursion
# Write a recursive function fibonacci(n) that returns the nth Fibonacci number (0-indexed, with fibonacci(0) = 0 and fibonacci(1) = 1).
def fibonnaci(n):
    if n <= 1:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)
print(fibonnaci(6))
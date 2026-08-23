#Nearest Palindrome
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def next_palindrome(n):
    num = n + 1
    while not is_palindrome(num):
        num += 1
    print("Nearest palindrome:",num)
number = int(input("Enter the number:"))
next_palindrome(number)
# Question 1 — Strings
# Write a function count_vowels(s) that returns the number of vowels (a, e, i, o, u — case-insensitive) in a given string.
def count_vowels(s):   ##first approach
    cnt = 0
    vowels = "aeiouAEIOU"
    for ch in s.lower():
        if ch in vowels:
            cnt += 1
    return cnt
print(count_vowels("Hello World"))


def count_v(s):    ##second approach
    return sum(1 for ch in s.lower() if ch in "aeiou")
print(count_v("Hello programming"))


# Question 2 — Lists
# Write a function remove_duplicates(nums) that returns a new list with duplicates removed, preserving the original order of first appearance.
def remove_duplicates(nums):
    result = []
    seen = set()
    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result
print(remove_duplicates([1, 3, 2, 3, 1, 5]))


# Question 3 — Dictionaries
# Write a function merge_dicts(d1, d2) that merges two dictionaries. If a key exists in both, add their values together.
def merge_dicts(d1, d2):
    result = dict(d1)
    for key, value in d2.items():
        result[key] = result.get(key,0) + 1
    return result
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))



# Question 4 — Recursion
# Write a recursive function sum_digits(n) that returns the sum of the digits of a non-negative integer n.
def sum_digits(n):   ##recursive function
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
print(sum_digits(12345))


def sum_digits(n):   ##iterative function
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
print(sum_digits(12345))


# Question 5 — OOP & Error Handling
# Design a class BankAccount with:

# __init__(self, balance=0) — starts with an optional initial balance
# deposit(amount) — adds to the balance (raise ValueError if amount is negative)
# withdraw(amount) — subtracts from the balance (raise ValueError if amount exceeds balance or is negative)
# get_balance() — returns the current balance

# Then write a snippet that creates an account, makes a few deposits/withdrawals, and demonstrates the error handling with a try/except.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative value")
        self.balance += amount
        print(f"{amount} credited successfully")
    
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative value")
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
        print(f"{amount} debited successfully")
    
    def get_balance(self):
        return self.balance

ba = BankAccount()
ba.deposit(2000)
ba.withdraw(500)
print("Balance:",ba.get_balance())
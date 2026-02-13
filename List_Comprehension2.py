#1. Convert string to uppercase
str1 = "programming"
result = "".join([ch.upper() for ch in str1])
print(result)


##2. Extract vowels from string
str1 = "programming"
vowels = "aeiou"
result = [ch for ch in str1 if ch in vowels]
print(result)


##3. Count vowels
str1 = "programming"
vowels = "aeiou"
result = len([ch for ch in str1 if ch in vowels])
print(result)

##4. Remove spaces from string
str1 = "p y t h o n"
result = "".join([ch for ch in str1 if ch != " "])
print(result)


##5. Reverse a string
str1 = "python"
result = "".join([str1[i] for i in range(len(str1)-1,-1,-1)])
print(result)


##6. Get ASCII values of characters
s = "are"
result = [ord(ch) for ch in s]
print(result)


##7. Replace vowels with *
str1 = "programming"
vowels = "aeiou"
result = "".join(["*" if ch in vowels else ch for ch in str1 ])
print(result)

##8. Extract digits from string
s = "a1b2c3"
result = [ch for ch in s if ch.isdigit()]
print(result)


##9. Convert list of strings to uppercase
list1 = ["python","java","javascript"]
result = "".join([ch.upper() for ch in list1])
print(result)


##10. Filter words greater than length 4
lst = ["doctor","kites","sun","two"]
result = [ch for ch in lst if len(ch) > 4]
print(result)


##11. Flatten list of characters from words
lst = ["python", "java"]
result = [ch for c in lst for ch in c]
print(result)


##12. Generate list of squares
result = [x*x for x in range(6)]
print(result)


##13. Even numbers from list
lst = [1,2,3,4,5,6,7,8,9,10]
result = [n for n in lst if n % 2 == 0]
print(result)
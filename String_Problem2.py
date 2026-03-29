#1)Write a Python program to print each character of a string on a new line.
string = "Hello world"
for s in string:
    print(s)

#2)Write a program to find the length of a string without using len().
string = "Hello World"
cnt = 0
for s in string:
    cnt += 1
print("Length of the string:",cnt)


#3)Write a Python program to convert a string to uppercase and lowercase.
string = "heLlo WoRld"
print(string.upper())
print(string.lower())


#4)Write a program to count the number of vowels in a string.
string = "python programming is easy"
vowel = "aeiouAEIOU"
cnt = 0
for s in string:
    if s in vowel:
        cnt += 1
print("Number of vowels:",cnt)


#5)Write a Python program to count the number of consonants in a string.
string = "hello world"
vowel = "aeiouAEIOU"
cnt = 0
for s in string:
    if s.isalpha() and s not in vowel:
        cnt += 1
print("Consonants:",cnt)


#6) Write a program to check whether a string is empty or not.
string = " "
if string == " ":
    print("Empty string")
else:
    print("Not empty string")

#7)Write a Python program to concatenate two strings.
str1 = "hello "
str2 = "world"
print(str1 + str2)


#8)Write a program to remove all spaces from a string.
string = "he ll o wo r ld"
new_str = ""
for s in string:
    if s != " ":
        new_str += s
print(new_str)


#9)Write a Python program to replace all occurrences of a character with another character.
string = "hello world"  #first approach
result = ""
for s in string:
    if s == 'l':
        result += 'm'
    else:
        result += s
print(result)


final = "".join(['m' if s == 'l' else s for s in string])  #second approach
print(final)


#10)Write a program to check whether a character is present in a string.
string = "hello of you"
ch = input("Enter the character to search:")
if ch in string:
    print("Present")
else:
    print("Not present")
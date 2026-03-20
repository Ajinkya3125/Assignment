#1)Write a Python program to reverse a string.
string = "hello world"
reverse = "".join(reversed(string))
print(reverse)


#2)Write a program to check whether a string is a palindrome.
string = "madam"
reverse = "".join(reversed(string))
if string == reverse:
    print("Palindrome")
else:
    print("Not palindrome")


#3)Write a Python program to count the number of vowels in a string.
string = "programming"
vowel = "aeiouAEIOU"
cnt = 0
for v in string:
    if v in vowel:
        cnt += 1
print("count of vowel:",cnt)


#4)Write a program to count the frequency of each character in a string.
string = "hello world"
freq = {}
for ch in string:
    freq[ch] = freq.get(ch,0) + 1
print(freq)


#5)Write a Python program to replace spaces in a string with hyphens (-).
string = "hello world"  #first approach
s1 = ""
for s in string:
    if s == " ":
        s1 += "-"
    else:
        s1 += s
print(s1)

replace_hyphen = string.replace(" ","-")  #second approach
print(replace_hyphen)


#6)Write a Python program to convert the first letter of each word to uppercase.
string = "this is a building"  #first approach
first_upper = " ".join([word.capitalize() for word in string.split()])
print(first_upper)

print(string.title())  #second approach


#7)Write a program to remove all special characters from a string.
string = "he@ll#o wor!l$d"  #first approach
special = "!@#$%^&*"
result = ""
for s in string:
    if s not in special:
        result += s
print(result)

result = "".join([s for s in string if s not in special]) #second approach
print(result)


#8)Write a Python program to find the longest word in a sentence.
sentence = "this is a pineapple and I like watermelon"
word = sentence.split()
largest = max(word,key=len)
print(largest)


#9)Write a program to check if two strings are anagrams.
str1 = "listen"
str2 = "silent"
print(sorted(str1) == sorted(str2))


#10)Write a program to find the first non-repeating character in a string.
string = "programming"
for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character:",ch)
        break
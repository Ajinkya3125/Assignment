#1)Write a Python program to check whether two strings are anagrams.
str1 = "tensil"
str2 = "silent"
if(len(str1) != len(str2)):   #first approach
    print("Not anagram")
else:
    freq = {}
    
    for ch in str1:
        freq[ch] = freq.get(ch,0) + 1
        
    for ch in str2:
        freq[ch] -= 1
        
    if all(v == 0 for v in freq.values()):
        print("Anagram")
    else:
        print("Not anagram")
        
        
if (sorted(str1.lower()) == sorted(str2.lower())): #second approach
    print("Anagram")
else:
    print("Not Anagram")


#2)Write a Python program to compress a string (e.g., "aaabb" → "a3b2").
string = "aaabb"
result = ""
cnt = 1
for i in range(len(string)):
    if i < len(string)-1 and string[i] == string[i+1]:
        cnt += 1
    else:
        result += string[i] + str(cnt)
        cnt = 1
print(result)


#3)Write a program to expand a compressed string (e.g., "a3b2" → "aaabb").
string = "a3b2"
result = ""
for i in range(0,len(string),2):
    char = string[i]
    count = int(str(string[i+1]))
    result += char * count
print(result)


#4)Write a program to count digits, letters, and special characters in a string.
string = "a1cd34gh5@8$#we"
digit = 0
letters = 0
special = 0
for ch in string:
    if ch.isdigit():
        digit += 1
    elif ch.isalnum():
        letters += 1
    else:
        special += 1
print("Number of digits:",digit)
print("Number of letters:",letters)
print("Number of special characters:",special)


#5)Write a program to remove all special characters from a string.
string = "abcd@ef$%"
result = ""
for ch in string:
    if ch.isalnum():
        result += ch
print(result)
        

#6)Write a program to find all substrings of a string.
string = "abc"
substring = [string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
print(substring)


#7)Write a Python program to find the first non-repeating character in a string.
string = "programming"
for ch in string:
    if string.count(ch) == 1:
        print("First non repeating character:",ch)
        break
    
    
#8)Write a Python program to check if one string is a rotation of another.
s1 = "abcd"
s2 = "dcbe"

if len(s1) == len(s2) and s2 in (s1+s1):
    print("Rotation")
else:
    print("Not Rotation")
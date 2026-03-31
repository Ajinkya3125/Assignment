#1)Write a Python program to reverse a string.
string = "hello world"
result = ""
for s in string:
    result = s + result
print(result)


#2)Write a program to check whether a string is a palindrome.
string = "madam"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


#3)Write a Python program to count the frequency of each character in a string.
string = "This is a python language"
freq = {}
for s in string:
    freq[s] = freq.get(s,0) + 1
print(freq)


#4)Write a program to find the first occurrence of a character in a string.
string = "programming"
for s in string:
    if string.count(s) == 1:
        print("First occurences character:",s)
        break

#5)Write a Python program to find the last occurrence of a character in a string.
string = "hello world"
print(string.rfind("l"))


#6)Write a program to remove duplicate characters from a string.
string = "hello world"
dup = []
for s in string:
    if s not in dup:
        dup.append(s)
print("".join(dup))


#7)Write a Python program to find the longest word in a sentence.
sentence = "this apple is red but watermelon is also red"
longest = max(sentence.split(), key=len)
print("Longest word:",longest)


#8)Write a program to find the shortest word in a sentence.
sentence = "this is a pineapple and I like watermelon"
shortest = min(sentence.split(), key=len)
print("Shortest word:", shortest)

#9)Write a Python program to count the number of words in a string.
string = "this is a big house"
word = string.split()
cnt = 0
for s in word:
    cnt += 1
print(cnt)


#10)Write a program to capitalize the first letter of each word in a string.
string = "this is a house and this is a car"
result = " ".join([s.capitalize() for s in string.split()])
print(result)
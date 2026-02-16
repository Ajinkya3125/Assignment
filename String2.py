##String examples
##1. Reverse a string
str1 = "Hello World"  ##first approach
print(str1[::-1])

rev = ""  ##second approach
for ch in str1:
    rev = ch + rev
print(rev)


##2. Check palindrome
s = "madam"
rev = s[::-1]
print(s == rev)


##3. Count vowels in a string
s = "pythOn programmIng"
vowel = "aeiou"
cnt = 0
for ch in s:
    if ch.lower() in vowel:
        cnt += 1
print(cnt)


##4. Count words in a sentence
s = "Welcome to the python tutorial"
cnt = 1
for ch in s:
    if ch == " ":
        cnt += 1
print(cnt)


##5. Remove duplicate characters
s = "hello to all"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)


##6. Find frequency of characters
s = "hello to all of you"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0) + 1
print(freq)


##7. Check anagram
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))


##8. Find first non-repeating character
s = "aabbcdde"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
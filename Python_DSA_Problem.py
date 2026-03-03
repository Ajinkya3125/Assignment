##Python DSA problems
#1)Reverse a string
s = "Hello World"   ##first approach
print(s[::-1])
##time complexity-:O(n)


s = "Hello World"  ##second approach without using slicing.
rev = []
for ch in s:
    rev.insert(0,ch)
print("".join(rev))
##time complexity-:O(n)


s = "Hello World"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
##time complexity-:O(n)^2


#2)Anagram Check
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))
#time complexity-:O(nlogn)


def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch,0) + 1
        
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

s1 = "listen"
s2 = "silent"
print(is_anagram(s1,s2))
#time complexity-:O(n)


#3)First Non-Repeating Character
def first_occur(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
        
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
    
s = "aabbcdd"
print(first_occur(s))
##time complexity-:O(n)


##4)Frequency Count
def count_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    return freq
s = "programming"
print(count_freq(s))
##time complexity -:O(n)
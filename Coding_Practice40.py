#Q1. Find All Even Numbers in a List
def find_evens(nums):
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    return even
print(find_evens([1, 2, 3, 4, 5, 6, 7, 8]))


#Q2. Count Vowels in a String Using a Dictionary
def vowel_count(s):
    vowels = "aeiouAEIOU"
    freq = {}
    for ch in s.lower():
        if ch in vowels:
            freq[ch] = freq.get(ch,0) + 1
    return freq
print(vowel_count("Programming is Amazing"))


#Q3. Find the Minimum Element in a List
def find_min(nums):
    min_num = nums[0]
    for n in nums:
        if n < min_num:
            min_num = n
    return min_num
print(find_min([8,3,9,2,6]))


#Q4. Check if Two Lists Have Any Common Elements
def has_common_element(list1, list2):
    for l1 in list1:
        if l1 in list2:
            return True
    return False
print(has_common_element([1,2,3],[4,5,3]))


#Q5. Capitalize the First Letter of Each Word
def capitalize_words(sentence):
    result_words = []
    words = sentence.split()
    for word in words:
        first_char = word[0]
        if 'a' <= first_char <= 'z':
            first_char = chr(ord(first_char) - 32)
        new_word = first_char + word[1:]
        result_words.append(new_word)
    return " ".join(result_words)
print(capitalize_words("the quick brown fox"))


#Q6. Invert a Dictionary (Swap Keys and Values)
def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted
print(invert_dict({"a": 1, "b": 2, "c": 3}))


#Q7. Remove a Given Character from a String
def remove_char(s,ch):
    result = ""
    for c in s:
        if c != ch:
            result += c
    return result
print(remove_char("hello world","o"))


#Q8. Find the Sum of List Elements at Even Indices
def sum_even_indices(lst):
    total = 0
    for i, n in enumerate(lst):
        if i % 2 == 0:
            total += n
    return total
print(sum_even_indices([10,20,30,40,50]))


#Q9. Check if a Dictionary is Empty
def is_dict_empty(d):
    if d == {}:
        return True
    return False
print(is_dict_empty({"a":1}))


#Q10. Find the Most Frequent Word in a Sentence
def most_frequent_word(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
    max_word = None
    max_count = 0
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word
print(most_frequent_word("the cat sat on the mat the cat ran"))
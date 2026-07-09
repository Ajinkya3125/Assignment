#Part A: Counter

#Q1)Use Counter to count the frequency of characters in:
from collections import Counter
string = "programming"
print(Counter(string))


#Q2)Use Counter to count the frequency of words in:
from collections import Counter
sentence = "python java python c java python"
words = sentence.split()
print(Counter(words))


#Q3)Find the most frequent character in:
from collections import Counter
string = "mississippi"
counter = Counter(string)
most_frequent = counter.most_common(1)
print(most_frequent)


#Q4)Use Counter to find the 2 most common elements.
from collections import Counter
nums = [1,2,2,3,3,3,4,4,4,4]
counter = Counter(nums)
second_common = counter.most_common(2)
print(second_common)


#Q5)Use Counter to count occurrences of numbers in:
from collections import Counter
num = [10,20,10,30,20,10]
print(Counter(num))


#Part B: defaultdict
#Q6)Use defaultdict(list) to group names by their first letter.
from collections import defaultdict
names = ["Ajinkya", "Amit", "Rahul", "Rohan", "Priya", "Roshan"]
groups = defaultdict(list)
for name in names:
    groups[name[0]].append(name)
print(dict(groups))


#Q7)Use defaultdict(list) to store all marks of each student.
from collections import defaultdict
data = [
("Ajinkya", 80),
("Ajinkya", 90),
("Rahul", 75)
]
groups = defaultdict(list)
for name, mark in data:
    groups[name].append(mark)
print(dict(groups))


#Q8)Count the frequency of characters in:
from collections import defaultdict
string = "banana"
freq = defaultdict(int)
for s in string:
    freq[s] += 1
print(dict(freq))


#Q9)Sum Values by Key
from collections import defaultdict
data = [("A",10),("B",20),("A",15),("B",5)]
result = defaultdict(int)
for key, value in data:
    result[key] += value
print(dict(result))


#Q10)Group Even and Odd Numbers
from collections import defaultdict
nums = [1,2,3,4,5,6,7,8]
result = defaultdict(list)
for num in nums:
    if num % 2 == 0:
        result["Even"].append(num)
    else:
        result["Odd"].append(num)

print(dict(result))


#Part C: deque
#Q11)Create:deque([10,20,30]) and Perform: append(40), appendleft(5)
from collections import deque
lst = [10,20,30]
dq = deque(lst)
dq.append(40)
dq.appendleft(5)
print(dq)


#Q12)Remove Elements in the deque([10,20,30,40,50]) and perform pop() and popleft() and print the remaining deque
from collections import deque
lst = [10,20,30,40,50]
dq = deque(lst)
dq.pop()
dq.popleft()
print(dq)


#Q13)Reverse a deque:
from collections import deque
lst = [1,2,3,4,5]
dq = deque(lst)
dq.reverse()
print(dq)


#Q14)Rotate a deque:
from collections import deque
lst = [1,2,3,4,5]
dq = deque(lst)
dq.rotate(2)
print(dq)


#Q15)Queue Simulation Using deque, implement: enqueue and dequeue
from collections import deque
queue = deque()

def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")
    
def dequeue():
    if queue:
        print(f"\nDequeued: {queue.popleft()}")
        
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()


#Q16)Find the first non-repeating character using Counter.
from collections import Counter
string = "swiss"
counter = Counter(string)
for s in counter:
    if counter[s] == 1:
        print("First non-repeating character:",s)
        break


#Q17)Find all elements that occur exactly once in:
from collections import Counter
nums = [1,2,2,3,4,4,5]
counter = Counter(nums)
result = []
for n in counter:
    if counter[n] == 1:
        result.append(n)
print(result)


#Q18)Use Counter to compare whether two strings are anagrams.
from collections import Counter
str1 = "listen"
str2 = "silent"
if Counter(str1) == Counter(str2):
    print(True)
else:
    print(False)
    
    
#Q19)Use defaultdict(list) to group words by their length.
from collections import defaultdict
words = ["cat","dog","python","java","go"]
df = defaultdict(list)
for word in words:
    df[len(word)].append(word)
print(dict(df))


#Q20)Using deque, check whether a string is a palindrome.
from collections import deque
string = "madam"
dq = deque(string)

if dq == deque(reversed(dq)):
    print("Palindrome")
else:
    print("Not Palindrome")
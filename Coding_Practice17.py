#Q1)Write a Python program to find the sum of all odd numbers in a list.
lst = [1,2,3,4,5,6,7]
result = sum([l for l in lst if l % 2 != 0])
print(result)

#Q2)Write a Python program to find the largest odd number in a tuple.
tup = (10, 25, 8, 17, 30)  #First approach
result = max([t for t in tup if t % 2 != 0])
print(result)

tup = (10, 25, 8, 17, 30)   #Second approach
max_odd = tup[0]
for t in tup:
    if t > max_odd and t % 2 != 0:
        max_odd = t
print(max_odd)


#Q3)Write a Python program to count how many values in a dictionary are greater than 50.
dic = {"A":40, "B":60, "C":80, "D":20}
cnt = 0
for key, value in dic.items():
    if value > 50:
        cnt += 1
print("Count of values greater than 50:",cnt)


#Q4)Write a Python program to check whether two sets have at least one common element.
A = {1,2,3}
B = {3,4,5}
if A.intersection(B):
    print("Common element exists")
else:
    print("Common element doesn't exists")
    
    
#Q5)Write a Python program to count the number of words that start with a vowel in a sentence.
sentence = "apple banana orange umbrella mango elephant"
words = sentence.split()
vowel = "aeiouAEIOU"
cnt = 0
for word in words:
    if word[0] in vowel:
        cnt += 1
print(cnt)


#Q6)Write a function find_average(lst) that returns the average of all elements in a list.
def find_average(lst):
    total = 0
    n = len(lst)
    for l in lst:
        total += l
    return total / n
print(find_average([10,20,30,40]))


#Q7)Write a function using *args to return the count of even numbers passed as arguments.
def count_event(*args):
    cnt = 0
    for a in args:
        if a % 2 == 0:
            cnt += 1
    return cnt
print(count_event(1,2,3,4,5,6))


#Q8)Write a recursive function to find the product of first n natural numbers.
def product_n(n):
    if n == 0:
        return 1
    else:
        return n * product_n(n-1)
print(product_n(5))


#Q9)Create a class Movie with:
# title
# rating
# Create a method is_hit() that returns:True, if rating ≥ 8, otherwise:False
class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
        
    def is_hit(self):
        if self.rating >= 8:
            return True
        else:
            return False

movie = Movie("Pushpa 2",7.5)
print(movie.is_hit())


#Q10)Use lambda and filter() to extract all numbers that are greater than 100.
lst = [50, 120, 80, 200, 30, 150]
result = list(filter(lambda x:x > 100, lst))
print(result)


#Q11)Write a Python program to find the first unique word in a sentence.
sentence = "python java python c java cpp"
words = sentence.split()
for word in words:
    if words.count(word) == 1:
        print(word)
        break
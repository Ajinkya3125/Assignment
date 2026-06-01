#Q1)using filter() function
data = [0,1,False,True,"Python",""]
filtered_data = list(filter(None, data))
print(filtered_data)

#Q2)Adding of three numbers using map() function
a,b,c = map(int, input().split())
sum = a + b + c
print(sum)

#Q3)finding negative numbers.
lst = [1,3,13,45,-2,0,-4,2,8,-6,-4,3,1,-67,90]  #first approach
if any(n < 0 for n in lst):
    print("Negative Numbers found")
else:
    print("No Negative Numbers found")
    
    
lst = [1,3,13,45,-2,0,-4,2,8,-6,-4,3,1,-67,90]  #second approach
for i in lst:
    if i < 0:
        print("Negative Numbers found")
        break
else:
    print("No Negative Numbers found")
    
    
#Q4)List comprehension and Generator expression for finding even numbers.
x = [i for i in range(100) if i % 2 == 0]
print(x)

y = (i for i in range(100) if i % 2 == 0)
print(y)


#Q5)Nested for loop
for i in range(3):
    print("*")
    for j in range(i+1):
        print(i, end=" ")
print()
        
#Q6)while loop
n = 10
while n > 0:
    print(n)
    n = n - 3
else:
    print("Ok")
    
    
#Q7)global and local variable
x = 10 #Global variable
def display():
    x = 100  #Local variable
    print(x)

def getData():
    print(x)
    
display()
getData()


#Q8)String concatenation
lst = ["Hello","this","is","a","python","language"] #first approach
string = ""
for s in lst:
    string = string+" "+s
print(string)

st = " ".join(lst)  #Second approach
print(st)


#Q9)using lambda expression and input() function
print("Addition of two numbers:",(lambda a,b:a+b)(int(input("Enter the first number:")),int(input("Enter the second number:"))))


#Q10)using '==' operator and 'is' keyword
lst1 = [1,2,3]
lst2 = [1,2,3]

print(lst1 == lst2) #== -> check values
print(lst1 is lst2) #is -> checks memory location
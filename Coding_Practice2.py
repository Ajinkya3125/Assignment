#Q1)Length of the string
print(len("Hello\n"))

#Q2)Shallow copy
l1 = [1,2,3,4]
l2 = l1
l2.append(5)
print(l1)
print(l2)
l3 = l1.copy()
l3.append(6)
print(l1)
print(l3)

#Q3)if-else condition
num = int(input("Enter the number:"))
if num % 2:
    print("Even")
else:
    print("Odd")
    
    
#Q4)function
def display(msg):
    print("Hello " + msg)
display("world")

#Q5)find greatest common divisor of the two numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

while num2 != 0:
    num1,num2 = num2, num1%num2
print("Greatest common divisor:",num1)


#Q6)print() function
print("3"+"4"*2)


#Q7)
a = "3"
a *= 2

print(int(a) + 5)

#Q8)
print(3**2**3)


#Q9)Check the prime number or not
n = int(input("Enter the number:"))
i = 2
while i <= n//2:
    if n % i == 0:
        print("Not Prime number")
        break
    i += 1
else:
    print("Prime Number")
    
    
#Q10)fliping the dictionary
dict1 = {"Ramesh":10000,"Ketan":20000,"Mohit":30000}
flip_result = {v:k for k,v in dict1.items()}
print(flip_result)
#Part A: Basics of Regex

#Q1)Write a Python program using re.findall() to extract all digits from:
import re
text = "Python123 Java456 C789"
digit = re.findall(r'\d+',text)
print(digit)


#Q2)Extract all words from:
import re
text = "Python is easy to learn"
result = re.findall(r'[a-zA-Z]+',text)
print(result)


#Q3)Use re.search() to check whether:
sentence = "I am learning Python"
if re.search("Python", sentence):
    print("Word found")
else:
    print("Word Not found")
    
    
#Q4)Use re.match() to check whether the string starts with:
import re
sentence = "Hello World"
if re.match("Hello", sentence):
    print("Matched")
else:
    print("Not Matched")
    
    
#Q5)Extract all vowels from string and using re.findall().
import re
string = "Programming"
result = re.findall(r'[aeiouAEIOU]+',string)
print(result)


#Part B: Number-Based Problems

#Q6)Extract all numbers from:
import re
sentence = text = "Order 123 costs 450 rupees and item 56 costs 200 rupees"
result = re.findall(r'\d+',sentence)
print(result)


#Q7)Find how many digits are present in:
import re
string = "abc123xyz45"
result = len(re.findall(r'\d',string))
print(result)


#Q8)Extract only 4-digit numbers from:
import re
word_sentence = "123 4567 89 1234 56789"
result = re.findall(r'\b\d{4}\b',word_sentence)
print(result)


#Q9)Extract all numbers ending with:
import re
numbers = "15 22 35 40 55 63"
result = re.findall(r'\b\d*5\b',numbers)
print(result)


#Q10)Extract decimal numbers from:
import re
sentence = "Price: 99.50, Discount: 12.75, Tax: 18"
result = re.findall(r'\d+\.\d+',sentence)
print(result)


#Part C: Email Validation
#Q11)Check whether: email is a valid email using regex.
# import re
# email = input("Enter the email:")
# result = r'^[a-zA-Z0-9.%+-]+@gmail\.com$'
# if re.findall(result, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")
    
    
#Q12)Extract all email addresses from:
import re
sentence = "Contact us at support@gmail.com or admin@yahoo.com"
result = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',sentence)
print(result)


#Q13)Count the number of email addresses present in:
import re
sentence = "a@gmail.com b@yahoo.com c@hotmail.com"
result = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',sentence)
print(len(result))


#Part D: Phone Number Extraction
#Q14)Extract all 10-digit phone numbers from:
import re
number = "Call 9876543210 or 9123456789"
result = re.findall(r'[\b\d{8}\b]+',number)
print(result)


#Q15)Check whether the given mobile number is valid or Not.
import re
number = "9865472990"
if re.fullmatch(r'[6-9]\d{9}',number):
    print("Valid Number")
else:
    print("Invalid Number")
    
    
#Part E: Interview Logic Questions
#Q16)Extract all hashtags from:
import re
sentence = "I love #Python and #Programming"
result = re.findall(r'#\w+',sentence)
print(result)


#Q17)Extract Words Starting with Capital Letters.
import re
sentence = "Ajinkya lives in Pune and studies Python"
result = re.findall(r'\b[A-Z]\w+',sentence)
print(result)


#Q18)Find all repeated digits in:
import re
number = "1122334455"
result = re.findall(r'\d{2}+',number)
print(result)


#Q19)Write a regex to validate a password that:
#i)Has at least 8 characters
#ii)Contains one uppercase letter
#iii)Contains one lowercase letter
#iv)Contains one digit
import re
password = input("Enter the password:")
result = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
if re.fullmatch(result, password):
    print("Valid Password")
else:
    print("Invalid Password!")
    
    
#Q20)Extract dates from:
import re
sentence = "Today is 25-06-2026 and tomorrow is 26-06-2026"
result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b',sentence)
print(result)
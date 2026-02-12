#String
s1 = 'apple red'
s2 = "Apple"
s3 = """Apple"""
s4 = " "

print(s1[0])  #indexing 0 ->A
print(s2[-1]) #indexing -1 ->e
print(s3)  
print(s1[1:4]) #ppl
print(s1[2:4]) #pl
print(s1[1:])  #pple
print(s1[:4])  #Appl
print(s2[::-1])

#String methods-case conversion
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.capitalize())

#Checking Methods
print(s1.isalpha()) #False
print(s1.isdigit()) #False
print(s1.isalnum())
print(s4.isspace())
print(s1.islower())
print(s1.isupper())

#Search methods
print(s1.find('a'))
print(s1.index('a'))
print(s1.count('p'))

#Replace & Modify
print(s1.replace('a','m'))
print(s2.strip())
print(s2.rstrip())
print(s2.lstrip())
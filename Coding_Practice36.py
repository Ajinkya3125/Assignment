#1)Number Triangle with Repeated Rows
def print_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print()
print_pattern(5)


#2)Hollow Diamond
def print_hollow_diamond(n):
    for i in range(n):
        spaces = n - i - 1
        print(' ' * spaces, end="")
        if i == 0:
            print('*')
        else:
            print('*' + ' ' * (2*i-1) + '*')
            
    for i in range(n-2,-1,-1):
        spaces = n - i - 1
        print(' ' * spaces, end="")
        if i == 0:
            print('*')
        else:
            print('*' + ' ' * (2*i-1) + '*')
        
print_hollow_diamond(5)


#3)Number Pyramid with Palindrome Rows
def print_palindrome_pyramid(n):
    for i in range(1,n+1):
        spaces = n - i
        ascending = "".join(str(num) for num in range(1,i+1))
        descending = "".join(str(num) for num in range(i-1,0,-1))
        rows = ascending + descending
        print(" " * spaces + rows)
print_palindrome_pyramid(5)




#The above questions based on list comprehension and enumerate() method

lst = ["1","2","a","3"]
result = [int(x) for x in lst if x.isdigit()]
print(result)


d = {"a":1,"b":2,"c":3}
lst = [(k,v) for k,v in d.items()]
print(lst)


lst = ['a','b','c']
result = [x for x,v in enumerate(lst)]
print(result)


lst = ['a','b','c']
for i,v in enumerate(lst):
    lst[i] = v.upper()
print(lst)


lst = [1,2,3,4,5]
for i in range(len(lst)):
    print(i, lst[i])
    
    
def square(x):
    return x * x
result = [square(x) for x in range(4)]
print(result)


lst = [0,1,"",[],"python",[1,2]]
result = [x for x in lst if x]
print(result)
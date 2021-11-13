### TUPLE

#Tuple is immutable
#Creating a tuple
a=(1,2,3,4,5)
a=1,2,3,4 #This also creates a tuple
# a[0]=1 # Error

def func(*args):
    print(args)

func(1,2,3,4,5)

# swap the values (works only on numbers) --> placement ques.
# Method -1
a=5
b=9
a=a+b
b=a-b
a=a-b
print(a,b)
# Logic require to understand the next Method
a=1,2
c, d= a # left side should have the same no. of variables as the number of elements in tuple
print(c)
print(d)
# Method -2
a=5
b=7
b,a =a,b
#This will swap the value
print(a)
print(b)

# List to tuple and tuple to list
a=(1,2,3)
print(type(a))
a=list(a)
print(type(a))

# Extras:String to List
a=list("Apoorv")
print(a)
a=tuple("Apoorv")
print(a)

# With the help of tuple we can return multiple value
def addsub(a,b):
    return a+b,a-b
x=addsub(1,2)
print(x)
print(type(x))
summ,diff=addsub(5,6)
print(summ,diff)

# NOT Tuple comprehension but generator object
a=(i**2 for i in range(10))
print(a) # output --> <generator object <genexpr> at 0x7f9874f7acf0>
#creating a List
a=[]
a=list()
a=[1,2,3,4]

## List is ordered, mutable, heterogenous and acecessible through index

a=["jatin",1,1.2]

# Basic operations on List
#Length of list
len(a)
# Concatenate the list
a + a
# Repetition
a * 5
# Membership in List
"jatin" in a
# "in" is a membership operator
# Iteration in list
for x in a:
    print(x)
# Indexing and list slicing
a=[1,2,3,4]
a[3]
# Pythons list and string supports negative indexing
a[-1]
# In Slicing start is included and last is excluded
print(a[::-1]) # This reverse the strings
# To check a string is palindrome or not
a="radar"
print(a == a[::-1])
### Updating a List
a=[1,2,3,4,5]
# Insert takes two argument index and element
a.insert(1,"jatin")
#Append
a.append("Garg") # add an element at the last of list

### Deleting list element
a=[1,2,3,4,5]
# By default pop function removes the last element but if an valid index is passed as an argument ,the corresponding element will be removed
a.pop()
a.pop(2)
a=["jatin","apoorv","bipin"]
# remove function removes the element by taking the name of the element as a parameter
a.remove("jatin")
# del is an statement is python
del a[1]
del a
#Sorting and reversing
a=[43,23,135,6,33,25]
# sorted function takes the data structure as an argument and returns a sorted list
sorted(a)
# sort function does not return any =thing , it makes changes in the list itself
a.sort()

for i in reversed(a):
    print(i)

a.reverse()

# map, strip and split function in list







# Comprehension --> a method to create list, set and dictionary in a single line of python
a=[]
for i in range(10):
    a.append(i**2)
print(a)

# List Comprehension
# x is a variable that will get append in the list

a=[x for x in range(10)]
print(a)

# These statement can also have nested loop and if else statment

a=[i**2 for i in range(10) if i % 2 ==0 ]
print(a)










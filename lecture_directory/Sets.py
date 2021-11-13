# SETS
# Sets is an unordered collection of objects
# These are used when the existence of an object
# in a collection is more important
# than the order or how many times it occurs
# There is no indexing in Sets
# Creating A Set
a= {1,2,3,4}
# This creates a set
# not a dict since keys are not defined.
# we cannot create an empty set by a={} (this is a dict )
# to create an empty set
a= set()
print(type(a))

a={1,2,3,4}
b={3,4,5,6}
print("Interesection -->",a.intersection(b))
print("Union -->",a.union(b))
print(a-b) # a-b --> a but not b
# iteration on set
for i in a:
    print(i)
a={1,2,3,4,1,23,4}
print(a)
# To de-duplicate the list , convert list into set
a=[1,2,31,2,3,2,31,1,4,22,23]
a=set(a)
print(a)

# Sets comprehension
x={ i**2 for i in range(10) if i % 2 == 0}


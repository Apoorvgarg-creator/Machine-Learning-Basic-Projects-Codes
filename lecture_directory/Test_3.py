### Some String operation
a=1
b=2
c=3
print(str(a)+"-"+str(b)+"-"+str(c))
# The above Method is a lot of hardwork which is unnecessary
# SOL- %d gets replace by the corresponding number
print("%d-%d-%d" % (a,b,c))
a=1
b=2
c=3.4
print(str(a)+"-"+str(b)+"-"+str(c))
# The above Method is a lot of hardwork which is unnecessary
# SOL- %d gets replace by the corresponding number
print("%d-%d-%d" % (a,b,c)) # The result would be 1-2-3 Since the format specifier  is int type
print("%d-%d-%0.1f%%f" %(a,b,c))
print("{}-{}-{}".format(a,b,c))
#We can also change the order of format by passing the indices
print("{1}-{2}-{0}".format(a,b,c))
# we can also pass name parameter
print("{lastname},{firstname}".format(firstname="Apoorv",lastname="Garg"))

# With current updates , It has become more simpler
#Example-
firstname="Apoorv"
lastname="garg"
print(f"{lastname},{firstname}") # This shows python is a powerful language
#Strip operation on Strings
# Strip removes the white spaces from both the sides of string
a="     jatin"
print(a)
print(a.strip())
# The difference is clear with the above example
a=input()
print(a =="yes")
print( a.strip()=="yes")
#Split operation on Strings
a=input()
a.split(" ") # returns a list in which each element would split into another if a space is present between them
a="jatin"
# a[0]= "1" ---> Error: String is immutable
# To change the string
a.replace("j","l")
abc="aaaaabffbdddccaa"
abc.replace("a","x")
# All the a will be replaced with x
# To count the frequency of a character in string ,We can use count function
abc.count('a') # ---> returns the frequency of char a in the String abc
abc.count("aaa") # output will be 1 since overlapping is not allowed in this count function

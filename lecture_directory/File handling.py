# File handling
# Open a file
file = open("hello.txt", "r")
# if we pass an argument in read() method i.e. 5, then it will read only 5 byte
# print(file.read())
print(file.read(5))
# closing a file
file.close()

# Writing to a file
file = open("something.txt", "w")
# write() method returns the number of bytes that are written in a file
print(file.write("hello Apoorv, How are you?"))
file.close()

# Reading from a file
file = open("hello.txt", "r")
# we can use one method at a time since the cursor place gets changes
# readlines() creates a list of all the lines
print(file.readlines())

# readline() method reads one line at a time
# print(file.readline())
# print(file.readline())
# print(file.readline())
file.close()


# Moving the cursor
# by default, when python opens a file the cursor is at the beginning of a file
file = open("hello.txt", "r")
file.read(5)  # read the first 5 character of file
# After this the cursor will point after the first 5 character
# So, if we use another read method , the first 5 character will not be included

file.seek(0)  # Now the cursor will again point at the beginning of a file

# Smarter way of opening a file
# With the "with" statement, you get better syntax and exceptions handling
# " The "with" statement simplifies exception handling by encapsulating common preparation and cleanup tasks."
# In addition, it will automatically close the file. the " With" statement provides a way
# for ensuring that a clean-up is always used

with open("hello.txt", "r") as file:
    print(file.read())
    file.seek(5)
    print(file.read())
# The file can be access only under the "with" block

# Error handling
# Error and Exceptions
# Error : Syntax not followed, and error doesn't allow the program to run
# Exceptions: Error detected during execution are called exceptions and are not unconditionally fatal

# example - Exception
# print(10/0)

# Exception handling-->
# try --> whatever is in try block tries to get executed if there is an error ,it ignores the try block
# except
def div(a, b):
    try:
        print(a/b)
    except:
        print("Error")


div(10, 0)


# Smarter way of handling exception
# print(10/0)
try:
    print(10/0)
except ZeroDivisionError:
    print("you were trying to divide by zero")

try:
    print(10/0)
    a = int("jatin")
except ZeroDivisionError:  # this except block is now only assigned to a particular type of error
    print("you were trying to divide by zero")
except ValueError:
    print("Value error occurred")
except: # this except blocks handles all the exception other than the above
    print("Some error occurred")

# Exception --> It is a base class defined in python that handles all type of error and exception in python

try:
    print(10/0)
except Exception as e:  # e is an object that stores the exception
    print(type(e))
    print(str(e))

# We can create our own exception

# raise statement
try:
    raise Exception("My custom error", 1, 2)  # this line shows that there is some error
except Exception as e:
    print(e.args)


class MyException:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    raise MyException("some error")
except Exception as e:
    print(str(e))  # this will not print the message "some error" since except blocks accepts error from Exception class
    # My Exception class must inherit the base class for Exception


class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    raise MyException("some error")
except Exception as e:
    print("error")
    print(str(e))

# More python statement that are use in exception handling
# else : will always execute if the try block didn't threw any error
# finally : As the name suggest, this block will always get executed no matter what
# finally block is use to have cleanup code , like closing a file etc.
try:
    print("hello world")
except:
    print("error")
else:
    print("woah")
finally:
    print("bye bye world")

try:
    print(10/0)
except:
    print("error")
else:
    print("woah")
finally:
    print("bye bye world")

def func():
    try:
        return 1
    finally:
        return 2


print(func())  # result --> 2


def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3


print(func())  # result --> 1


def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4


print(func())  # result --> 4


# "with" statement have pre defined cleanup action

# "with" "statement have 2 dunder
class A:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

   # To implement a class with "with" statement the below 2 dunders are mandatory

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(args)  # args are the error or exception raised inside this with block
        return True  # exception will not be raise during execution


with A(5) as a:
    print(str(a))
    # print(10/0)
    raise 10/0


print("hello")







































# OOPS
# Encapsulation --> combining all the attributes common in a class
# Abstraction --> hiding the features (like how it works) from the users
# Inheritance --> child class  can inherit the properties of parent class
# Polymorphism --> Many forms, given object can exist in multiple forms
# In python, everything is treated as an object
a = 1
print(isinstance(a, object))  # result --> True
a = "Apoorv"
print(isinstance(a, object))  # result --> True
a = [1, 2, 3, 4]
print(isinstance(a, object))  # result --> True
a = print
print(isinstance(a, object))  # result --> True
# A minimal example of a class


class Person:
    pass


p = Person()  # p is an object (create an instance of class)

print(isinstance(p, object))  # result --> True
print(p)  # result --> <__main__.Person object at 0x7fde6c25ab50>
# main is the module in which the class exist
print(id(p))
print(hex(id(p)))  # memory address

# In python, there is a flag whether a function ic callable or not
# function and class objects are callable
# int and float  are not callable
# what happens when we call function , it starts executing the code written inside it
# what happens when we call class , it creates an instance of class

# class with method


class Person:
    name = "Apoorv"

    def say_hi(self):
        print("Hello my name is", self.name)


p = Person()
p.say_hi()  # In this way, p automatically gets assign as a parameter

# In python , this can also be done since in the function say_hi we pass self as an argument
Person.say_hi(p)  # In this way, p manually gets assign as a parameter

# Special method in Python
# The init method
# The special method gets call as soon as an object of class is created
# Special method are not constructor


class Person:
    # not a constructor

    def __init__(self, name):
        print("new object")
        self.name = name
        pass

    def say_hi(self):
        print("Hello my name is", self.name)


p = Person("Apoorv")
p.say_hi()


# Dunders or Magic function
# __init__ is a dunder
# __init__ --> called when object is created
# __del__ --> called when object is deleted
# __add__ --> add have two parameter (self,other) other can be a object of any class
# __add__ --> calling can be done by a+b --> a.__add__(b)
# __str__ --> helps us convert the object to string --> calling can be done by str(object name) --> a.__str__()
# __eq__ -->  calling can be done by a==b --> a.__eq__(b)


class Car:
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def __str__(self):
        return "{} {}".format(self.model, self.mileage)

    def __repr__(self):
        return "{}".format(self.model)

    def __eq__(self, other):
        return self.mileage == other.mileage

    def __add__(self, other):
        return self.mileage + other.mileage


c1 = Car('a', 2)
c2 = Car('b', 2)
print(c1 + c2)
print(c1 == c2)

# implement C++ function in python
# cout << "Apoorv"


class Ostream:
    def __lshift__(self, other):
        print(other, end=" ")
        return self

    def __rshift__(self, other):
        self.name = other
        return self

    def say_hi(self):
        print()
        print("My name is", self.name)


cout = Ostream()

cout << "Apoorv" << "Garg"
cout >> "Appy"
cout.say_hi()


# Common mistakes


class Dog:
    kind = "canine"

    def __init__(self, name):
        self.name = name


a = Dog("MAX")
b = Dog("Oscar")
print("a kind --> ", a.kind)
print("b kind --> ", b.kind)
print(id(a.kind) == id(b.kind))  # result --> True
b.kind = "Lebra"
print("b kind --> ", b.kind)  # No changes will take place in a kind since string is immutable
print("a kind --> ", a.kind)
print("After the above operation")
print(id(a.kind) == id(b.kind))  # result --> False


class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_tricks(self, tricks):
        self.tricks.append(tricks)


a = Dog("Max")
b = Dog("Oscar")

a.add_tricks("fetch")
a.add_tricks("talk")
print(a.tricks)
print(b.tricks)  # Since list is a mutable , changes in a lead changes in b as well

# "tricks" memory is shared among all the objects
print(id(a.tricks) == id(b.tricks) == id(Dog.tricks))  # result --> True

# To correct this mistake define trick inside the init method because init method is called after creating a object
# hence new memory address will be assigned to every behaviour


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = list()

    def add_tricks(self, tricks):
        self.tricks.append(tricks)


a = Dog("Max")
b = Dog("Oscar")

a.add_tricks("fetch")
a.add_tricks("talk")
print(a.tricks)
print(b.tricks)

print(id(a.tricks) == id(b.tricks))  # result --> False

# Inheritance


class SchoolMember:
    """ Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        """Tell my details"""
        print("Name: \"{}\" Age: \"{}\"".format(self.name, self.age))


class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: \"{:d}\"".format(self.salary))


class Student(SchoolMember):
    """Represents a Student"""

    def __init__(self, name, age, marks):
        super().__init__(name, age)  # super method finds the function in base class and call it
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        super().tell()
        print("Marks: \"{:d}\"".format(self.marks))


t = Teacher("Mr. Ujjwal", 40, 30000)
t.tell()
s = Student("Apoorv", 25, 95)
s.tell()

# Overloading --> Python doesn't support overloading
# Overriding --> Python supports overriding
# overriding means replacing the old version of function with the current version


# Method Resolution order (MRO)
# C3 Linearization


class A:
    # x = 10
    pass


class B(A):
    x = 10


class C(A):
    pass


class D(C):
    x = 5


class E(B, D):
    pass

print(E.x)
print(E.__mro__)  # returns the tuple that contains the order in which inheritance will be consider
# according to C# linearization

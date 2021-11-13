# Dictionary

# List and tuple are ordered data structure
# dictionary are unordered data structure

# creating a dictionary
a={ "name":"Appy",
    "marks": 100 ,
    "subjects" : ["maths","data structure"],
    "friends" : {
        "jatin" : "Web dev"
    }
}
# Some Important dict method
# get()
# items()
# keys()
# values()
# clear()

# Iteration over dict
# by default , keys are return in dict
for key in a:
    print(key,a.get(key))

# item() method create a tuple of key, value pairs
for item in a.items():
    print(item)

# keys () method returns keys
for key in a.keys():
    print(key)
# value() method returns the values
for value in a.values():
    print(value)

# get() method returns the associated value if key is present and if the key is invalid it returns None
# clear() method removes all the content of dict and returns an empty dict
# Keys in the dictionary can be ANY immutable data structure
a={
    (1,2):"jatin"
}
print(a[(1,2)])

# dict comprehension
# i is the key
# i**2 is the value
# nested loop and if else can also be use
a={ i : i**2 for i in range(10)}




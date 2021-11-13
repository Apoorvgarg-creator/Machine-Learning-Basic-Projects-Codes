# JSON files
# javascript Object notation abbreviated as JSON is a light-weight data interchange format.
# It encode python objects as JSON strings and decode JSON strings into Python objects

# Old method --> XML


# json.dump(obj,fileObj) : Serializes obj as a JSON formatted stream to fileObj
# json.dumps(obj) : Serializes obj as JSON formatted string
# json.load(JSONfile) : De-serializes JSONfile to a python object
# json.loads(JSONfile) : DE-serializes JSONfile(type:string) to a python object


with open("data.json", "r") as file:
    x=file.read()
    file.seek(0)
    print(file.read())
print("variables defined under","\"with\"","block are global")
print(x)
# Reading from a json file
import json
with open("data.json", "r") as file:
    d = json.load(file)
    print(type(d))
    print(d["name"])
    print(d["subjects"][0])
print("d is global")
print(d["subjects"][1])
with open("data.json", "r") as file:
    data = file.read()
    print(data)
    d= json.loads(data) # This d is global
    print(type(d))
# writing to a json file

string=json.dumps(d)
print(type(string))
with open("data2.json", "w") as file:
    json.dump(d,file)


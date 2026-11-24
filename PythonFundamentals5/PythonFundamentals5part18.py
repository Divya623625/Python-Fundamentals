import json

data = {
    "name" : "Divya",
    "age" : 19,
    "isTeacher" : True
}

with open("data1.json","w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
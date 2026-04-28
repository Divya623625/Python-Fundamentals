import json
py_obj1 = {
    "name" : "Divya",
    "isTeacher" : None
}
print(type(py_obj1))
json_str1 = json.dumps(py_obj1)
print(json_str1, type(json_str1))

json_str = '{"name" : "Divya", "IsTeacher": true}'
print(type(json_str))
py_obj = json.loads(json_str)
print(py_obj, type(py_obj)) 
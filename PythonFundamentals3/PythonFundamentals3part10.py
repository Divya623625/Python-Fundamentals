info = {
    "name" : "Divya",
    "cgpa" : 9.81,
    "subjects" : ["math","science"],
    "PI" : 3.14
}
dict_keys = info.keys()
print(dict_keys)
print(type(dict_keys))
print(info.values())
print(info.items())

print(info["name"])
print(info.get("cgpa"))

# This key does NOT exist → Error (program stops here)
# So "End of code" will NOT print
# print(info["cgpa2"])
# print("End of code")

# dict.get(key) → returns None 
print(info.get("cgpa3"))
print("End of code")

info.update({
    "city" : "Delhi"
})

print(info)
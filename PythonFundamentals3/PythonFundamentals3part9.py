# A dictionary stores data in key : value pairs.
# Dictionaries are mutable

info = {
    "name" : "Divya",
    "cgpa" : 9.81,
    "subjects" : ["math","science"],
    "PI" : 3.14
}
print(info["name"])
print(info["PI"])
print(info["subjects"])
print(info["cgpa"])

info["cgpa"] = 10
print(info["cgpa"])
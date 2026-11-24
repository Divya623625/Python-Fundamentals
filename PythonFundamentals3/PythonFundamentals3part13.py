# Given a list of tuples with info(name,subject)-
# List all the unique courses
# List students enrolled in English
# Create dictionary (student, set of courses)

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

unique_courses = set()

# 1.
for tup in info:
    unique_courses.add(tup[1]) # courses

print(unique_courses)

# 2.
for name,course in info:
    if course == "English":
        print(name)

# 3. 
dict = {}
for name,course in info:
    if (dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)



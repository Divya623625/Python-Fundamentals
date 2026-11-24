# Given a list,print all elements that appear more than once in the list.
# use sets
list = [1,1,2,2,3,4,5,4,6,5,6,7,7,9,10]
seen = set()
duplicates = set()

for element in list:
    if element in seen:
        duplicates.add(element)
    else:
        seen.add(element)
        
print(duplicates)
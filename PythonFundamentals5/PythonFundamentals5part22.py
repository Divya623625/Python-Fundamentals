# Create a Python dictionary of 3 cities and their populations. Save it to "cities.json"
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population - update this info in the json file.

import json

# Step 1: create dictionary
cities = {
    "Bangalore": 12000000,
    "Mumbai": 20000000,
    "Delhi": 19000000
}

# save to JSON file
with open("cities.json", "w") as f:
    json.dump(cities, f)

# Step 2: load and print
with open("cities.json", "r") as f:
    data = json.load(f)

print("Cities and Population:")
for city, pop in data.items():
    print(city, ":", pop)

# Step 3: add new city
new_city = input("Enter new city: ")
new_pop = int(input("Enter population: "))

data[new_city] = new_pop

# update JSON file
with open("cities.json", "w") as f:
    json.dump(data, f)

print("Updated successfully!")
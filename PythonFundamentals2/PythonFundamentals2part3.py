# if-elif-else
"""
elif means else if
Used to check multiple conditions one by one
if is checked first -> if it fails,elif is checked.
if all conditions fail,else runs
only one block executes
This is called if-elif-else ladder
"""
# Write a python program that takes a traffic light color as input(red,green or yellow) and prints the correct action
"""
If the color is red, Print Stop
If the color is green, Print Go
If the color is yellow, Print look
For any other input, print Wrong color for traffic lights.
"""
color = input("Enter color: ")
if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("look")
else:
    print("wrong color for traffic lights")

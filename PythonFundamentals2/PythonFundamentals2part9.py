# Match Case - alternate for if-elif-else
# Color Value input - case green - go
# Color Red - Stop
# Color Yellow - Look
color=input("Enter color: ")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _: # default case
        print("Wrong color!")
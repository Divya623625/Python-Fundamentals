# Create a dictionary where:
# keys = student names
# Values = marks(integer)
# Write a menu based program where user presses a key ('A','B','C','D')
# depending on the operation they want to perform on the dictionary
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks
 
student = {
    "Divya" : 99,
    "Sushmitha" : 100,
    "Ramya" : 89,
    "Hamsa" : 97,
    "Manasa" : 57,
    "Yashoda" : 99,
    "Alice" : 67,
    "Charlie" : 58
}

while True:
    print("1. Add a student")
    print("2. Update marks")
    print("3. Search for a student")
    print("4. Display all the students")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in student:
            marks = int(input("Enter new marks: "))
            student[name] = marks
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in student:
            print(name, "marks =", student[name])
        else:
            print("Student not found")

    elif choice == 4:
        for name in student:
            print(name, ":", student[name])

    elif choice == 5:
        break

    else:
        print("Invalid choice")

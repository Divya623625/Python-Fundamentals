# Concept: Encapsulation
# Create a class Student with private attributes _name, _roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 & 100 & name cannot be empty).

class Student:
    def __init__(self, name, roll_no, marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

    # Setter (with validation)
    def set_name(self, name):
        if name != "":
            self._name = name
        else:
            print("Name cannot be empty")

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Roll no must be 1 to 100")

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Marks cannot be negative")

    # Getter
    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks


# Example
s1 = Student("Divya", 10, 80)

s1.set_marks(90)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())
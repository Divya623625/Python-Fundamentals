# Concept: Instance & Class Attributes
# Create a class Player with:
# • a class variable player_count
# • instance variables name and level
# Track how many players were created.

class Player:
    player_count = 0   # class variable

    def __init__(self, name, level):
        self.name = name      # instance variable
        self.level = level    # instance variable
        Player.player_count += 1   # increase count


# Objects
p1 = Player("A", 1)
p2 = Player("B", 2)
p3 = Player("C", 3)

print("Total players:", Player.player_count)
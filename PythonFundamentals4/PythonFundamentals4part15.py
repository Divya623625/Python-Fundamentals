# Concept - Classes and Objects

# Create a class Book with the following attributes:
# • title
# • author
# • list of reviews
# And add methods to:
# • add a new review
# • count reviews
# • display all reviews

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for r in self.reviews:
            print(r)


# Object
b1 = Book("Python", "ABC")

b1.add_review("Good")
b1.add_review("Easy")

print(b1.count_reviews())
b1.display_reviews()
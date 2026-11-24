# Design and create an online store for Products(name, price)
# Track total products being created
# Create a static method to calculate discount on each product based on a % parameter.

class Product:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self): #instance method
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"Final discounted price = {price - (price * discount/100)}")
P1 = Product("Phone", 10_000)
P2 = Product("Laptop", 50_000)
P3 = Product("Pen", 10)

P1.get_info()
P2.get_info()
P3.get_info()

Product.get_count()

P1.calc_discount(P1.price,12)
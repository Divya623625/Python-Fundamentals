# Types of Methods
# Class Methods
# Instance Methods
# Static Methods

class laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted price = {final_price}")

l1 = laptop("16gb", "512gb")
l2 = laptop("8gb" , "256gb")

l1.get_info()
laptop.get_storage_type()

laptop.calc_discount(40_000, 10)
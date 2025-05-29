
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return NotImplemented
    

class Smartphone(Product):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Smartphone Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

    def __str__(self):
        return f"Smartphone Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"
    
class Laptop(Product):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Laptop Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

    def __str__(self):
        return f"Laptop Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

item1 = Product("Laptop", 1500)
item2 = Product("Laptop", 1500)
item3 = Product("Smartphone", 800)
item4 = Smartphone("Apple", "iPhone 14", 999)
print(item1)
print(item2)
print(item3)
print(item4)

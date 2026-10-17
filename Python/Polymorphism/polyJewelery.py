#Challenge:
# Redo your Jewellery(Product) challenge from Module 3 if you haven’t yet: 
# Jewellery adds weight and a method price_per_gram(). 
# Then override total_value() in Jewellery so it returns price * quantity plus a 5% making charge, 
# and loop through a mixed list of Product and Jewellery objects printing each total. 
# # This is polymorphism with the code you’ve already built.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

class Jewellery(Product):
    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight = weight

    def price_per_gram(self):
        return self.price / self.weight

    def total_value(self):
        return super().total_value() * 1.05
    

items = [Product("pen", 10, 5), Jewellery("ring", 1000, 2, 5)]

for item in items:
    print(item.name, item.total_value())
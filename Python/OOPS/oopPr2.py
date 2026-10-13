#Practice B: 
# Add a method total_value() to your Product class (name, price, quantity) that returns price * quantity. 
# Create 3 products in a list and use a loop with a running total to print the combined value.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1=Product("chocolate",10,10)
p2=Product("icecream",20,20)
p3=Product("muffin", 30,30)

products = [p1,p2,p3]

total = 0
for items in products:
    value = items.total_value()
    print("Item name: ", value)
    total += value

print("combined total: ", total )
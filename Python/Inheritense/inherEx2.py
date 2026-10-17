# Exercise 2 (super):
# Create a class Vehicle with brand and speed (default 0). 
# Create a child class Car that adds an attribute

class Vehicle:
    def __init__(self, brand, speed=0):
        self.brand=brand
        self.speed=speed

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

car1 = Car('supra', 100, 2)
print(car1.brand)
print(car1.speed)
print(car1.doors)


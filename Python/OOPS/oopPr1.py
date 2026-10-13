class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return f"{self.brand} is going {self.speed} km/h"

car1 = Car("Toyota")
car1.accelerate(50)
car1.brake(20)
print(car1)        # Toyota is going 30 km/h
car1.brake(100)
print(car1)        # Toyota is going 0 km/h
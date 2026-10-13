class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius * self.radius

    def cir(self):
        return 2 * self.pi * self.radius

c1 = Circle(20)
c2 = Circle(40)

print("area: ", c1.area())
print("circumference: ", c1.cir())
print("\n")
print("area: ", c2.area())
print("circumference: ", c2.cir())
# Exercise 2 (shapes):
# Create a parent class Shape with a method area() returning 0. 
# Create children Rectangle (width, height), Square (side) and Triangle (base, height, 
# with area = 1/2 × base × height). Put one of each in a list, loop through, 
# and print each area with its class name. Hint: type(s).__name__ gives the class name as a string.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def area(self):
        return 1/2 * self.base * self.height

r = Rectangle(10,20)
s = Square(10)
t = Triangle(15,20)

shapes = [r,s,t]

for shape in shapes:
    class_name = type(shape).__name__
    print(f"{class_name} Area: {shape.area()}")

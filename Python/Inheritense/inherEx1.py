#Exercise 1:
#Create a class Animal with name and a method eat() that prints "<name> is eating". 
#Create a child class Dog with a method bark(). Create a Dog and call both eat() and bark().

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

d1 = Dog("leo")

d1.eat()
d1.bark()
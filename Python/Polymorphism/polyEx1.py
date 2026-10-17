# Exercise 1:
# Create classes Dog, Cat, and Cow, each with a method speak() that prints its sound. 
# Put one of each in a list and call speak() in a loop. 
# Then add a Duck class and add it to the list without changing the loop.

class Dog:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return "woof!"

class Cat:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return "Meow!"

class Cow:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return "Moo!"

dog = Dog("DOG")
cat = Cat("CAT")
cow = Cow("COW")

list = [dog, cat, cow]

for x in list:
    print(x.speak())

class Duck:
    def __init__(self, name):
        self.name=name

duck = Duck("DUCK")
list.append(duck)

print(" ")

for x in list:
    print(x.name)


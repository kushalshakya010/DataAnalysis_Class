class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'hi, im {self.name}, {self.age} years old.')

class Student(Person):
    def study(self):
        print(f'{self.name} is studying.')

kushal = Person('kushal', 22)
kushal.introduce()

liza = Student('liza', 20)
liza.introduce()
liza.study()


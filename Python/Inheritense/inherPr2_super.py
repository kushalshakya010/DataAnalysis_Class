class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)    # let Person set name and age
        self.grade = grade             # Student adds its own

s = Student("Liza", 20, "A")
print(s.name, s.grade)    # Liza A
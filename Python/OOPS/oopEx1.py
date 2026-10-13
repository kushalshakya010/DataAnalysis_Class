class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def is_pass(self):
        return self.marks >= 40

s1 = Student("Ram", 30)
s2 = Student('hari', 45)

print(s1.is_pass())
print(s2.is_pass())

class Student:
    def __init__(self, name):
        self.name=name

    def is_pass(marks):
        if marks >= 40:
            return "True"
        else:
            return "False"

s1 = Student("Ram")
s2 = Student('hari')

print(Student.is_pass(30))
print(Student.is_pass(45))

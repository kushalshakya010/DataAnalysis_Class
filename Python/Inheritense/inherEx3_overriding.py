# Exercise 3 (overriding):
# Create a class Employee with name and salary, and a method info() that prints "<name> earns <salary>". 
# Create a child class Manager that adds team_size and overrides info() to print "<name> earns <salary> and manages <team_size> people". Test both classes.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"{self.name} earns {self.salary} Rs")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        print(f"{self.name} earns {self.salary} Rs and manages {self.team_size} people")

print("- case one:")
ep1 = Employee("ram", 60000)
ep1.info()

print("- case two:")
man1 = Manager("laxman", 100000, 300)
man1.info()
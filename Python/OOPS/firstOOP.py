class Car : 
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


car1 = Car("suzuki","swift",2014)

car1.drive()


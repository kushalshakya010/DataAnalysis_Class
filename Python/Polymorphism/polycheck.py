class Printer:
    def show(self):
        print("Printing document")

class Scanner:
    def show(self):
        print("Scanning document")

class Fax:
    pass

for device in [Printer(), Scanner(), Fax()]:
    device.show()
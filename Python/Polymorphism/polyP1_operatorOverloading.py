class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"Rs {self.amount}"

a=Money(100)
b=Money(250)

print(a+b)

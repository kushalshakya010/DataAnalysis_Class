class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand=brand
        self.power_rating=power_rating
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already turned on.")
        else:
            self.turned_on = True
            print(f"{self.brand} microwave is now turned on.")

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f"{self.brand} microwave is now turned off.")
        else:
            print(f"{self.brand} microwave is already turned off.")

    def run(self, seconds:int) -> None:
        if self.turned_on:
            print(f'running ({self.brand}) for {seconds} seconds')
        else:
            print(f"{self.brand} microwave is turned off. Please turn it on before running.")

micro1 = Microwave(brand="sony", power_rating="B")

micro1.turn_on()
micro1.run(30)
micro1.turn_off()
micro1.run(10)


micro2 = Microwave(brand="samsung", power_rating="C")

micro2.turn_on()
micro2.run(30)
micro2.turn_off()
micro2.run(10)

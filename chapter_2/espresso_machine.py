from espresso import Espresso


class EspressoMachine:
    def __init__(self):
        self.price = 300000

    def make_espresso(self):
        return Espresso()

    def get_price(self):
        self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return "EspressoMachine"

from milk import Milk
from cafe_latte import CafeLatte


class Barista:
    def __init__(self):
        self.espresso_machine = None

    def set_espresso_machine(self, espresso_machine):
        self.espresso_machine = espresso_machine

    def make_espresso(self):
        return self.espresso_machine.make_espresso()

    def make_cafe_latte(self):
        espresso = self.espresso_machine.make_espresso()
        milk = Milk()

        cafe_latte = CafeLatte()

        cafe_latte.set_espresso(espresso)
        cafe_latte.set_milk(milk)

        return cafe_latte

    def __str__(self):
        return "Barista"

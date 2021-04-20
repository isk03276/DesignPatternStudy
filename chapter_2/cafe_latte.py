from icoffee import ICoffee


class CafeLatte(ICoffee):
    def __init__(self):
        self.name = "CafeLatte"

        self.espresso = None
        self.milk = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_espresso(self, espresso):
        self.espresso = espresso

    def set_milk(self, milk):
        self.milk = milk

    def display(self):
        print(self.name + " (" + str(self.espresso) + " + " + str(self.milk) + " )")

    def __str__(self):
        return "CaffeLatte"

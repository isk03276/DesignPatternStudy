from coffee import Coffee
from icoffee import ICoffee


class Espresso(ICoffee):
    def __init__(self):
        self.name = "Espresso"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def display(self):
        print(self.name)

    def __str__(self):
        return "Espresso"

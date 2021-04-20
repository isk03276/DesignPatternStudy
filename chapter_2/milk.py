from icoffee import ICoffee


class Milk(ICoffee):
    def __init__(self):
        self.name = "Milk"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def display(self):
        print(self.name)

    def __str__(self):
        return "Milk"

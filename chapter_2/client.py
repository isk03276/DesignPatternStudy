from coffee import Coffee
from espresso import Espresso
from barista import Barista
from espresso_machine import EspressoMachine


class Client:
    def main(self):
        barista = Barista()

        espresso_machine = EspressoMachine()

        barista.set_espresso_machine(espresso_machine)

        cafe_latte = barista.make_cafe_latte()

        cafe_latte.display()


if __name__ == "__main__":
    client = Client()
    client.main()

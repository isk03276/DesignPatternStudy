from calculator import Calculator
from add_operation import AddOperation
from substract_operation import SubstractOperation
from multiply_operation import MultiplyOperation
from divide_operation import DivideOperation
from calc_client import CalcClient
from display_client import DisplayClient


class Client:
    def main(self):
        calculator = Calculator()

        first_number = 100
        second_number = 20

        operation = AddOperation()

        calc_client = CalcClient()

        answer = calc_client.request(calculator, operation, first_number, second_number)

        print("answer = " + str(answer))

        display_client = DisplayClient()

        display_client.request(calculator, operation, first_number, second_number)


if __name__ == "__main__":
    client = Client()
    client.main()
from chapter_4.singleton.operation_singleton import OperationSingleton


class Client:
    def main(self):
        calculator_singleton = OperationSingleton()

        first_number = 100
        second_number = 20

        calculator_singleton.operate(OperationSingleton.ADD_OPERATION, first_number, second_number)
        calculator_singleton.operate(OperationSingleton.SUBSTRACT_OPERATION, first_number, second_number)
        calculator_singleton.operate(OperationSingleton.MULTIPLY_OPERATION, first_number, second_number)
        calculator_singleton.operate(OperationSingleton.DIVIDE_OPERATION, first_number, second_number)


client = Client()
client.main()

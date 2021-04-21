from idisplayable import IDisplayable


class Calculator(IDisplayable):
    def __init__(self):
        self.operation = None

    def calculate(self, first_number, second_number):
        if self.operation.is_invalid_number(first_number, second_number):
            return -999

        return self.operation.operate(first_number, second_number)

    def set_operation(self, operation):
        self.operation = operation

    def new_display(self, operation, first_number, second_number):
        answer = operation.operate(first_number, second_number)

        operator = operation.get_operator()

        print(str(first_number) + operator + str(second_number) + "=" + str(answer))
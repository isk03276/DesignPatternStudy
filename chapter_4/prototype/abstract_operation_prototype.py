import abc


class AbstractOperationPrototype(metaclass=abc.ABCMeta):
    def __init__(self, operation=None):
        if operation != None:
            self.first_number = operation.first_number
            self.second_number = operation.second_number
        else:
            self.first_number = 0
            self.second_number = 0

    @abc.abstractmethod
    def get_clone(self):
        pass

    def get_first_number(self):
        return self.first_number

    def set_first_number(self, first_number):
        self.first_number = first_number

    def get_second_number(self):
        return self.second_number

    def set_second_number(self, second_number):
        self.second_number = second_number

    def print_result(self, result):
        print(result)

    @abc.abstractmethod
    def get_answer(self, first_number, second_number):
        pass

    @abc.abstractmethod
    def get_operator(self):
        pass

    def operate(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        operator = self.get_operator()

        answer = self.get_answer(first_number, second_number)

        result = str(first_number) + operator + str(second_number) + " = " + str(answer)

        self.print_result(result)

import abc


class AbstractOperation(metaclass=abc.ABCMeta):
    def __init__(self):
        self.first_number = 0
        self.second_number = 0

    def operate(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        operator = self.get_operator()

        operator_description = operator.get_description()

        answer = operator.get_answer(first_number, second_number)

        result = str(first_number) + operator_description + str(second_number) + "=" + str(answer)

        self._print(result)

    @abc.abstractmethod
    def get_operator(self):
        pass

    def get_first_number(self):
        return self.first_number

    def set_first_number(self, first_number):
        self.first_number = first_number

    def get_second_number(self):
        return self.second_number

    def set_second_number(self, second_number):
        self.second_number = second_number

    def _print(self, result):
        print(result)

from abc import ABCMeta, abstractmethod


class AbstractOperationBuilder(metaclass=ABCMeta):
    def __init__(self, first_number, second_number):
        self.result = ""
        self.first_number = first_number
        self.second_number = second_number

    @abstractmethod
    def operate(self, first_number, second_number):
        pass

    @abstractmethod
    def build_operator(self):
        pass

    def build_first_number(self):
        self.result += str(self.first_number)

    def build_second_number(self):
        self.result += str(self.second_number)

    def build_answer(self):
        answer = self.operate(self.first_number, self.second_number)
        self.result += " = "
        self.result += str(answer)

    def get_result(self):
        return self.result

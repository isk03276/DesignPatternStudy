from abstract_operation_builder import AbstractOperationBuilder


class MultiplyOperationBuilder(AbstractOperationBuilder):
    def __init__(self, first_number, second_number):
        AbstractOperationBuilder.__init__(self, first_number, second_number)

    def operate(self, first_number, second_number):
        return first_number * second_number

    def build_operator(self):
        self.result += " * "
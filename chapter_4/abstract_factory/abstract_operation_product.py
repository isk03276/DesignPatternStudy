import abc


class AbstractOperationProduct(metaclass=abc.ABCMeta):
    def __init__(self):
        self.first_number_operand_product = None
        self.second_number_operand_product = None

    def set_first_number_operand_product(self, first_number_operand_product):
        self.first_number_operand_product = first_number_operand_product

    def set_second_number_operand_product(self, second_number_operand_product):
        self.second_number_operand_product = second_number_operand_product

    def add(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        return first_number + second_number

    @abc.abstractmethod
    def print_result(self):
        pass

    def get_first_number(self):
        return self.first_number_operand_product.get_number()

    def get_second_number(self):
        return self.second_number_operand_product.get_number()
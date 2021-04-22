from abstract_operation_product import AbstractOperationProduct


class IntegerOperationProduct(AbstractOperationProduct):
    def print_result(self):
        first_number = self.get_first_number()
        second_number = self.get_second_number()

        print(first_number, " + ", second_number, " = ", self.add())

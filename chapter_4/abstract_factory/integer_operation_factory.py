from abstract_operation_factory import AbstractOperationFactory
from integer_operation_product import IntegerOperationProduct
from integer_number_operand_product import IntegerNumberOperandProduct


class IntegerOperationFactory(AbstractOperationFactory):
    def create_operation_product(self):
        return IntegerOperationProduct()

    def create_number_operand_product(self, value):
        return IntegerNumberOperandProduct(value)

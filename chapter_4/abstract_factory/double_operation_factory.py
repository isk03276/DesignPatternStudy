from abstract_operation_factory import AbstractOperationFactory
from double_operation_product import DoubleOperationProduct
from double_number_operand_product import DoubleNumberOperandProduct


class DoubleOperationFactory(AbstractOperationFactory):
    def create_number_operand_product(self, value):
        return DoubleNumberOperandProduct(value)

    def create_operation_product(self):
        return DoubleOperationProduct()

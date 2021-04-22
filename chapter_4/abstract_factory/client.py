from integer_operation_factory import IntegerOperationFactory
from double_operation_factory import DoubleOperationFactory

class Client:
    def main(self):
        first_number = "10.3"
        second_number = "20.2"

        operation_factory = IntegerOperationFactory()

        operation_product = operation_factory.create_operation_product()
        operation_product.set_first_number_operand_product(operation_factory.create_number_operand_product(first_number))
        operation_product.set_second_number_operand_product(operation_factory.create_number_operand_product(second_number))

        operation_product.print_result()

        operation_factory = DoubleOperationFactory()

        operation_product = operation_factory.create_operation_product()
        operation_product.set_first_number_operand_product(operation_factory.create_number_operand_product(first_number))
        operation_product.set_second_number_operand_product(operation_factory.create_number_operand_product(second_number))

        operation_product.print_result()

client = Client()
client.main()

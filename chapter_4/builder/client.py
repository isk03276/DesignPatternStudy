from add_operation_builder import AddOperationBuilder
from substract_operation_builder import SubstractOperationBuilder
from multiply_operation_builder import MultiplyOperationBuilder
from divide_operation_builder import DivideOperationBuilder
from operation_director import OperationDirector


class Client:
    def main(self):
        first_number = 100
        second_number = 20

        operation_builders = []

        operation_builders.append(AddOperationBuilder(first_number, second_number))
        operation_builders.append(SubstractOperationBuilder(first_number, second_number))
        operation_builders.append(MultiplyOperationBuilder(first_number, second_number))
        operation_builders.append(DivideOperationBuilder(first_number, second_number))

        for operation_builder in operation_builders:
            operationDirector = OperationDirector(operation_builder)
            operationDirector.construct()


client = Client()
client.main()

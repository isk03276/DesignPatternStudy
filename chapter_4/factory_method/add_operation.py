from abstract_operation import AbstractOperation
from add_operator import AddOperator


class AddOperation(AbstractOperation):
    def get_operator(self):
        return AddOperator()
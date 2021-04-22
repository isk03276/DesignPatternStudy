from abstract_operation_prototype import AbstractOperationPrototype


class AddOperationPrototype(AbstractOperationPrototype):
    def __init__(self, operation = None):
        AbstractOperationPrototype.__init__(self, operation)

    def get_clone(self):
        return AddOperationPrototype(self)

    def get_answer(self, first_number, second_number):
        return first_number + second_number

    def get_operator(self):
        return "+"

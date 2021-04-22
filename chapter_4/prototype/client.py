from add_operation_prototype import AddOperationPrototype


class Client:
    def __init__(self):
        self.operation_prototype = None
        self.operation_prototype_map = {}
        self._init_operation_map()

    def operate(self):
        self.operation_prototype.operate()

    def set_operation(self, operator, first_number, second_number):
        self.operation_prototype = self.get_operation_clone(operator)

        self.operation_prototype.set_first_number(first_number)
        self.operation_prototype.set_second_number(second_number)

    def _init_operation_map(self):
        self.operation_prototype_map["+"] = AddOperationPrototype()

    def get_operation_clone(self, operator):
        operation = self.operation_prototype_map.get(operator)
        return operation.get_clone()

    def main(self):
        client = Client()

        first_number = 100
        second_number = 20

        client.set_operation("+", first_number, second_number)
        client.operate()


client = Client()
client.main()
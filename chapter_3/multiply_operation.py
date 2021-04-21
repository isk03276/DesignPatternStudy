from abstract_operation import AbstractOperation


class MultiplyOperation(AbstractOperation):
    def operate(self, first_number, second_number):
        answer = first_number * second_number

        return answer

    def get_operator(self):
        return "*"

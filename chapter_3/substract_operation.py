from abstract_operation import AbstractOperation


class SubstractOperation(AbstractOperation):
    def operate(self, first_number, second_number):
        answer = first_number - second_number

        return answer

    def get_operator(self):
        return "-"


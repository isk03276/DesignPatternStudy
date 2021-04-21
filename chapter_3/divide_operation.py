from abstract_operation import AbstractOperation


class DivideOperation(AbstractOperation):
    def operate(self, first_number, second_number):
        answer = first_number / second_number

        return answer

    def is_invalid_number(self, first_number, second_number):
        if second_number == 0:
            return True
        return False

    def get_operator(self):
        return "/"

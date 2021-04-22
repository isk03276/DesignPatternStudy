from abstract_operator import AbstractOperator


class AddOperator(AbstractOperator):
    def get_answer(self, first_number, second_number):
        return first_number + second_number

    def get_description(self):
        return " + "
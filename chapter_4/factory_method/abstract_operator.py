import abc


class AbstractOperator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_answer(self, first_number, second_number):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass

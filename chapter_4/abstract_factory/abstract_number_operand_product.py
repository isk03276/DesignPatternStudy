import abc


class AbstractNumberOperandProduct(metaclass=abc.ABCMeta):
    def __init__(self, value):
        self.value = value

    @abc.abstractmethod
    def get_number(self):
        pass

    def get_value(self):
        return self.value

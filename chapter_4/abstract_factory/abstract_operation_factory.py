import abc


class AbstractOperationFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_operation_product(self):
        pass

    @abc.abstractmethod
    def create_number_operand_product(self, value):
        pass

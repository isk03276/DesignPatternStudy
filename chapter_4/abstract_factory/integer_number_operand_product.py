from abstract_number_operand_product import AbstractNumberOperandProduct


class IntegerNumberOperandProduct(AbstractNumberOperandProduct):
    def __init__(self, value):
        AbstractNumberOperandProduct.__init__(self, value)

    def get_number(self):
        value = self.get_value()
        return int(float(value))

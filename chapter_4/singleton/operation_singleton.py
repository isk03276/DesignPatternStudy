class OperationSingleton:
    __instance = None

    ADD_OPERATION = 1
    SUBSTRACT_OPERATION = 2
    MULTIPLY_OPERATION = 3
    DIVIDE_OPERATION = 4

    @classmethod
    def get_instance(cls, *args, **kargs):
        if not cls.__instance:
            cls.__instance = cls(*args, **kargs)
        return cls.__instance

    def operate(self, operator_type, first_number, second_number):
        answer = 0
        operator = None

        if operator_type == OperationSingleton.ADD_OPERATION:
            answer = first_number + second_number
            operator = "+"
        elif operator_type == OperationSingleton.SUBSTRACT_OPERATION:
            answer = first_number - second_number
            operator = "-"
        elif operator_type == OperationSingleton.MULTIPLY_OPERATION:
            answer = first_number * second_number
            operator = "*"
        elif operator_type == OperationSingleton.DIVIDE_OPERATION:
            answer = first_number / second_number
            operator = "/"

        result = str(first_number) + operator + str(second_number) + "=" + str(answer)

        self.print_result(result)

    def print_result(self, result):
        print(result)

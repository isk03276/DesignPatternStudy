class OperationDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_first_number()
        self.builder.build_operator()
        self.builder.build_second_number()
        self.builder.build_answer()

        result = self.builder.get_result()

        self._print(result)

    def _print(self, result):
        print(result)

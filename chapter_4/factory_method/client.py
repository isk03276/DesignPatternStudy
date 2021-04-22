from add_operation import AddOperation


class Client:
    def main(self):
        first_number = 100
        second_number = 20

        operation = AddOperation()
        operation.set_first_number(first_number)
        operation.set_second_number(second_number)

        operation.operate()

client = Client()
client.main()
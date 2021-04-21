from abc import ABCMeta, abstractmethod


class IDisplayable(metaclass=ABCMeta):
    @abstractmethod
    def new_display(self, operation, first_number, second_number):
        pass

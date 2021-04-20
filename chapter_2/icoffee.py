from abc import ABCMeta, abstractmethod


class ICoffee(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def display(self):
        pass

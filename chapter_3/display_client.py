from idisplayable import IDisplayable


class DisplayClient:
    def request(self, displayable, operation, first_number, second_number):
        displayable.new_display(operation, first_number, second_number)
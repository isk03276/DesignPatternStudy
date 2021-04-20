from abstract_bounding_shape import AbstractBoundingShape


class RectangleShape(AbstractBoundingShape):
    def __init__(self, x, y, width, height):
        AbstractBoundingShape.__init__(self)
        """
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        """

    def draw(self):
        print("draw Rectangle")

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


if __name__ == "__main__":
    rectangle_shape = RectangleShape(0,0,0,0)


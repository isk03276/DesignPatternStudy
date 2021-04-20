from rectangle_shape import RectangleShape


class RoundRectangleShape(RectangleShape):
    shape_id_count = 0

    def __init__(self, arc_width, arc_height):
        self.arc_width = arc_width
        self.arc_height = arc_height

    def draw(self):
        print("draw RoundRectangle")

    def get_arc_width(self):
        return self.arc_width

    def set_arc_width(self, arc_width):
        self.arc_width = arc_width

    def get_arc_height(self):
        return self.arc_height

    def set_arc_height(self, height):
        self.height = height

    @classmethod
    def get_shape_id_counter(cls):
        cls.shape_id_count += 1
        return cls.shape_id_count


if __name__ == "__main__":
    print(RoundRectangleShape.shape_id_count)
    print(RoundRectangleShape.get_shape_id_counter())
    print(RoundRectangleShape.get_shape_id_counter())

    rectangle_shape = RectangleShape(0, 0, 0, 0)
    round_rectangle_shape = RoundRectangleShape(0, 0)
    rectangle_shape.draw()
    round_rectangle_shape.draw()





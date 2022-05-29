class Point:
    x : int
    y : int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    top_left : Point
    top_right: Point
    bottom_left : Point
    bottom_right : Point

    # В качестве параметров принимются кортеж (x, y)
    def __init__(self, top_left, top_right, bottom_right, bottom_left):
        self.top_left = Point(top_left)
        self.top_right = Point(top_right)
        self.bottom_right = Point(bottom_right)
        self.bottom_left = Point(bottom_left)

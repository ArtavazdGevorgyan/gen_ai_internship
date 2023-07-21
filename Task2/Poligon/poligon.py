
from point2D import Point2DSequence, Point2D


class Polygon:
    vertices = Point2DSequence(1, 10)

    def __init__(self, *vertices) -> None:
        self.vertices = list(vertices)

    def append(self, point) -> None:
        if isinstance(point,Point2D):
            self.vertices.append(point)
        else:
            raise TypeError(f"Type must be Point2D")

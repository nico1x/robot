class Coordinate:
    MAX_X = 4
    MAX_Y = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def within_bounds(self):
        return (
            self.x >= 0
            and self.x <= Coordinate.MAX_X
            and self.y >= 0
            and self.y <= Coordinate.MAX_Y
        )

    def tuple(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

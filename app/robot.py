from .coordinate import Coordinate
from .direction import Direction


class Robot:
    NEGATIVE_COORDINATE = Coordinate(-1, -1)

    def __init__(self):
        self.coordinate = Robot.NEGATIVE_COORDINATE
        self.direction = Direction.DEFAULT

    @property
    def placed(self):
        return (
            self.coordinate != Robot.NEGATIVE_COORDINATE
            and self.coordinate.within_bounds()
        )

    def place(self, coordinate, direction):
        if not coordinate.within_bounds():
            return
        self.coordinate = coordinate
        self.direction = direction

    def move(self):
        if not self.placed:
            return

        current_x, current_y = self.coordinate.tuple()

        coordinates = {
            Direction.NORTH: Coordinate(current_x, current_y + 1),
            Direction.SOUTH: Coordinate(current_x, current_y - 1),
            Direction.EAST: Coordinate(current_x + 1, current_y),
            Direction.WEST: Coordinate(current_x - 1, current_y),
        }

        new_coordinate = coordinates.get(self.direction, Robot.NEGATIVE_COORDINATE)

        if not new_coordinate.within_bounds():
            return

        self.coordinate = new_coordinate

    def left(self):
        if not self.placed:
            return

        directions = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }

        self.direction = directions.get(self.direction, Direction.DEFAULT)

    def right(self):
        if not self.placed:
            return

        directions = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }

        self.direction = directions.get(self.direction, Direction.DEFAULT)

    def report(self):
        if not self.placed:
            return
        print(f"{self.coordinate.x},{self.coordinate.y},{self.direction.value}")

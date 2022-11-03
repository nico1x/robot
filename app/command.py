from enum import Enum

from .direction import Direction


class Command(Enum):
    PLACE = "PLACE"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    REPORT = "REPORT"

    @staticmethod
    def parse_place(command):
        place = command.split(" ")

        if len(place) != 2:
            return None

        try:
            if Command(place[0]) != Command.PLACE:
                return None
        except ValueError:
            return None

        opts = place[1].split(",")

        if len(opts) != 3:
            return None

        x, y, direction = opts

        if not x.isdigit() or not y.isdigit():
            return None

        try:
            # ValueError is raised when direction is invalid.
            if Direction(direction) not in list(Direction):
                return None
        except ValueError:
            return None

        return int(x), int(y), Direction(direction)

    @staticmethod
    def validate(command):
        try:
            # ValueError is raised when command is invalid.
            if Command.parse_place(command) is None and Command(command) not in list(
                Command
            ):
                return False
        except ValueError:
            return False
        return True

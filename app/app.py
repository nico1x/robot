from .command import Command
from .coordinate import Coordinate
from .robot import Robot


class App:
    def run(self, filename):
        try:
            with open(filename, encoding="utf-8") as f:
                robot = Robot()
                for line in f.readlines():
                    command = line.rstrip()
                    if not Command.validate(command):
                        # Ignore invalid command.
                        continue

                    if place := Command.parse_place(command):
                        x, y, direction = place
                        coordinate = Coordinate(x, y)
                        robot.place(coordinate, direction)
                    elif Command(command) == Command.MOVE:
                        robot.move()
                    elif Command(command) == Command.LEFT:
                        robot.left()
                    elif Command(command) == Command.RIGHT:
                        robot.right()
                    elif Command(command) == Command.REPORT:
                        robot.report()

        except UnicodeDecodeError:
            print("Use text file only.")
        except FileNotFoundError:
            print("File not found.")

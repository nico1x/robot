import random
import unittest
from contextlib import redirect_stdout
from io import StringIO

from app import Coordinate, Direction, Robot


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_placed_true(self):
        self.robot.place(Coordinate(0, 0), Direction.NORTH)
        self.assertTrue(self.robot.placed)

    def test_placed_false(self):
        self.assertFalse(self.robot.placed)

    def test_place_success(self):
        for coordinate in [
            Coordinate(0, 0),
            Coordinate(2, 1),
            Coordinate(4, 3),
            Coordinate(1, 2),
        ]:
            direction = random.choice(list(Direction))
            self.robot.place(coordinate, direction)
            self.assertEqual(self.robot.coordinate, coordinate)
            self.assertEqual(self.robot.direction, direction)

    def test_place_false(self):
        for coordinate in [
            Coordinate(-1, 0),
            Coordinate(5, 1),
            Coordinate(4, 10),
            Coordinate(42, 2),
        ]:
            direction = random.choice(list(Direction))
            self.robot.place(coordinate, direction)
            self.assertEqual(self.robot.coordinate, Robot.NEGATIVE_COORDINATE)
            self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_move_success(self):
        for coordinate, direction in [
            (Coordinate(1, 1), Direction.NORTH),
            (Coordinate(2, 1), Direction.SOUTH),
            (Coordinate(3, 3), Direction.EAST),
            (Coordinate(1, 2), Direction.WEST),
        ]:
            self.robot.place(coordinate, direction)
            self.robot.move()

            if direction == Direction.NORTH:
                self.assertEqual(self.robot.coordinate.x, coordinate.x)
                self.assertEqual(self.robot.coordinate.y, coordinate.y + 1)
            elif direction == Direction.SOUTH:
                self.assertEqual(self.robot.coordinate.x, coordinate.x)
                self.assertEqual(self.robot.coordinate.y, coordinate.y - 1)
            elif direction == Direction.EAST:
                self.assertEqual(self.robot.coordinate.x, coordinate.x + 1)
                self.assertEqual(self.robot.coordinate.y, coordinate.y)
            elif direction == Direction.WEST:
                self.assertEqual(self.robot.coordinate.x, coordinate.x - 1)
                self.assertEqual(self.robot.coordinate.y, coordinate.y)

            self.assertEqual(self.robot.direction, direction)

    def test_move_not_within_bounds(self):
        for coordinate, direction in [
            (Coordinate(0, 4), Direction.NORTH),
            (Coordinate(2, 0), Direction.SOUTH),
            (Coordinate(4, 3), Direction.EAST),
            (Coordinate(0, 2), Direction.WEST),
        ]:
            self.robot.place(coordinate, direction)
            self.robot.move()
            self.assertEqual(self.robot.coordinate, coordinate)
            self.assertEqual(self.robot.direction, direction)

    def test_move_not_placed(self):
        self.robot.move()
        self.assertEqual(self.robot.coordinate, Robot.NEGATIVE_COORDINATE)
        self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_left_placed(self):
        self.robot.place(Coordinate(0, 0), Direction.NORTH)
        for direction in [
            Direction.WEST,
            Direction.SOUTH,
            Direction.EAST,
            Direction.NORTH,
        ]:
            self.robot.left()
            self.assertEqual(self.robot.direction, direction)

    def test_left_direction_none(self):
        self.robot.place(Coordinate(0, 0), None)
        self.robot.left()
        self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_left_not_placed(self):
        self.robot.left()
        self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_right_placed(self):
        self.robot.place(Coordinate(0, 0), Direction.NORTH)
        for direction in [
            Direction.EAST,
            Direction.SOUTH,
            Direction.WEST,
            Direction.NORTH,
        ]:
            self.robot.right()
            self.assertEqual(self.robot.direction, direction)

    def test_right_direction_none(self):
        self.robot.place(Coordinate(0, 0), None)
        self.robot.right()
        self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_right_not_placed(self):
        self.robot.right()
        self.assertEqual(self.robot.direction, Direction.DEFAULT)

    def test_report_placed(self):
        for coordinate, direction, expected in [
            (Coordinate(4, 1), Direction.NORTH, "4,1,NORTH\n"),
            (Coordinate(2, 3), Direction.SOUTH, "2,3,SOUTH\n"),
            (Coordinate(0, 3), Direction.EAST, "0,3,EAST\n"),
            (Coordinate(3, 4), Direction.WEST, "3,4,WEST\n"),
        ]:
            with StringIO() as stdout, redirect_stdout(stdout):
                self.robot.place(coordinate, direction)
                self.robot.report()
                self.assertEqual(stdout.getvalue(), expected)

    def test_report_with_move(self):
        for coordinate, direction, expected in [
            (Coordinate(4, 1), Direction.NORTH, "4,2,NORTH\n"),
            (Coordinate(2, 3), Direction.SOUTH, "2,2,SOUTH\n"),
            (Coordinate(0, 3), Direction.EAST, "1,3,EAST\n"),
            (Coordinate(3, 4), Direction.WEST, "2,4,WEST\n"),
        ]:
            with StringIO() as stdout, redirect_stdout(stdout):
                self.robot.place(coordinate, direction)
                self.robot.move()
                self.robot.report()
                self.assertEqual(stdout.getvalue(), expected)

    def test_report_with_right_and_move(self):
        for coordinate, direction, expected in [
            (Coordinate(3, 1), Direction.NORTH, "4,1,EAST\n"),
            (Coordinate(2, 3), Direction.SOUTH, "1,3,WEST\n"),
            (Coordinate(0, 3), Direction.EAST, "0,2,SOUTH\n"),
            (Coordinate(3, 3), Direction.WEST, "3,4,NORTH\n"),
        ]:
            with StringIO() as stdout, redirect_stdout(stdout):
                self.robot.place(coordinate, direction)
                self.robot.right()
                self.robot.move()
                self.robot.report()
                self.assertEqual(stdout.getvalue(), expected)

    def test_report_with_left_and_move(self):
        for coordinate, direction, expected in [
            (Coordinate(2, 2), Direction.NORTH, "1,2,WEST\n"),
            (Coordinate(4, 4), Direction.SOUTH, "4,4,EAST\n"),
            (Coordinate(4, 3), Direction.EAST, "4,4,NORTH\n"),
            (Coordinate(1, 3), Direction.WEST, "1,2,SOUTH\n"),
        ]:
            with StringIO() as stdout, redirect_stdout(stdout):
                self.robot.place(coordinate, direction)
                self.robot.left()
                self.robot.move()
                self.robot.report()
                self.assertEqual(stdout.getvalue(), expected)

    def test_report_not_placed(self):
        expected = ""
        with StringIO() as stdout, redirect_stdout(stdout):
            self.robot.report()
            self.assertEqual(stdout.getvalue(), expected)

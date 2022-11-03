import unittest

from app import Command, Direction


class TestCommand(unittest.TestCase):
    def test_validate_true(self):
        for command in ["MOVE", "LEFT", "RIGHT", "REPORT", "PLACE 0,0,NORTH"]:
            self.assertTrue(Command.validate(command))

    def test_validate_false(self):
        for command in [
            "MOVER",
            "LEFTWING",
            "RIGHTWING",
            "REPORTER",
            "PLACE X,Y,PLACE",
        ]:
            self.assertFalse(Command.validate(command))

    def test_parse_place_success(self):
        for place, expected in [
            ("PLACE 0,0,NORTH", (0, 0, Direction.NORTH)),
            ("PLACE 1,1,SOUTH", (1, 1, Direction.SOUTH)),
            ("PLACE 42,42,EAST", (42, 42, Direction.EAST)),
            ("PLACE 4,4,WEST", (4, 4, Direction.WEST)),
        ]:
            self.assertEqual(Command.parse_place(place), expected)

    def test_parse_place_returns_none(self):
        for place in [
            "MOVE 0,1,NORTH",
            "PLACER 0,0,NORTH",
            "PLACE A,1,SOUTH",
            "PLACE 42,B,EAST",
            "PLACE 4,4,WESTER",
        ]:
            self.assertIsNone(Command.parse_place(place))

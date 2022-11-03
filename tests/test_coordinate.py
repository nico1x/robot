import unittest

from app import Coordinate


class TestCoordinate(unittest.TestCase):
    def test_within_bounds_true(self):
        for coordinate in [
            Coordinate(0, 0),
            Coordinate(2, 1),
            Coordinate(4, 3),
            Coordinate(1, 2),
        ]:
            self.assertTrue(coordinate.within_bounds())

    def test_within_bounds_false(self):
        for coordinate in [
            Coordinate(-1, 0),
            Coordinate(42, 42),
            Coordinate(5, 5),
            Coordinate(1, 5),
        ]:
            self.assertFalse(coordinate.within_bounds())

    def test_tuple(self):
        coordinate = Coordinate(3, 2)
        self.assertEqual((3, 2), coordinate.tuple())

        coordinate = Coordinate(1, 4)
        self.assertEqual((1, 4), coordinate.tuple())

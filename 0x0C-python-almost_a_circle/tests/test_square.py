#!/usr/bin/python3
# test_square.py
"""Defines unittests for models/square.py."""


import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for Square class."""

    def test_area(self):
        """Test the calculation of the area."""
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_perimeter(self):
        """Test the calculation of the perimeter."""
        square = Square(5)
        self.assertEqual(square.perimeter(), 20)

    def test_side_setter(self):
        """Test the setter for the side attribute."""
        square = Square(5)
        square.side = 6
        self.assertEqual(square.side, 6)

    def test_side_getter(self):
        """Test the getter for the side attribute."""
        square = Square(5)
        self.assertEqual(square.side, 5)

    def test_invalid_side(self):
        """Test that an exception is raised for an invalid side."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str_representation(self):
        """Test the string representation of the square."""
        square = Square(5)
        self.assertEqual(str(square), "Square(side=5)")

    def test_equality(self):
        """Test the equality comparison between squares."""
        square1 = Square(5)
        square2 = Square(5)
        square3 = Square(6)
        self.assertEqual(square1, square2)
        self.assertNotEqual(square1, square3)

if __name__ == '__main__':
    unittest.main()

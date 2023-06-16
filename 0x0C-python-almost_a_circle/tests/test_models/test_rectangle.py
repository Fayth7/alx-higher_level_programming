#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py."""


import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for Rectangle class."""

    def test_area(self):
        """Test the calculation of the area."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_perimeter(self):
        """Test the calculation of the perimeter."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.perimeter(), 18)

    def test_width_setter(self):
        """Test the setter for the width attribute."""
        rectangle = Rectangle(4, 5)
        rectangle.width = 6
        self.assertEqual(rectangle.width, 6)

    def test_height_setter(self):
        """Test the setter for the height attribute."""
        rectangle = Rectangle(4, 5)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_width_getter(self):
        """Test the getter for the width attribute."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.width, 4)

    def test_height_getter(self):
        """Test the getter for the height attribute."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.height, 5)

    def test_invalid_width(self):
        """Test that an exception is raised for an invalid width."""
        with self.assertRaises(ValueError):
            Rectangle(-4, 5)

    def test_invalid_height(self):
        """Test that an exception is raised for an invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(4, -5)

    def test_str_representation(self):
        """Test the string representation of the rectangle."""
        rectangle = Rectangle(4, 5)
        self.assertEqual(str(rectangle), "Rectangle(width=4, height=5)")

    def test_equality(self):
        """Test the equality comparison between rectangles."""
        rectangle1 = Rectangle(4, 5)
        rectangle2 = Rectangle(4, 5)
        rectangle3 = Rectangle(6, 7)
        self.assertEqual(rectangle1, rectangle2)
        self.assertNotEqual(rectangle1, rectangle3)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class represents a square.

    Attributes:
        __size (float or int): The size of the square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0."""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square.

        Returns:
            float or int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have the same area, False otherwise."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares have different areas, False otherwise."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area of self is less than the area of other."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Less than or equal to comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area of self is less than or equal to the area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Greater than comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True ifarea of self is greater than the area of other."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Greater or equal to comparison operator for squares based on area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if area of self is greater or equal to area of other."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

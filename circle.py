import math


class Circle:
    """A class to represent a circle."""

    def __init__(self, radius: float):
        """
        Initialise Circle with a radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def perimeter(self) -> float:
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

    def area(self) -> float:
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2
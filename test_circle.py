import unittest
import math
from circle import Circle


class TestCircle(unittest.TestCase):
    """Unit tests for the Circle class."""

    def test_perimeter_positive_radius(self):
        """Test perimeter with a standard positive radius."""
        c = Circle(radius=5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5)

    def test_perimeter_zero_radius(self):
        """Test perimeter with radius of zero."""
        c = Circle(radius=0)
        self.assertAlmostEqual(c.perimeter(), 0)

    def test_perimeter_decimal_radius(self):
        """Test perimeter with a decimal radius."""
        c = Circle(radius=2.5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 2.5)

    def test_area_positive_radius(self):
        """Test area with a standard positive radius."""
        c = Circle(radius=5)
        self.assertAlmostEqual(c.area(), math.pi * 25)

    def test_area_zero_radius(self):
        """Test area with radius of zero."""
        c = Circle(radius=0)
        self.assertAlmostEqual(c.area(), 0)

    def test_area_decimal_radius(self):
        """Test area with a decimal radius."""
        c = Circle(radius=2.5)
        self.assertAlmostEqual(c.area(), math.pi * 2.5 ** 2)


if __name__ == '__main__':
    unittest.main()
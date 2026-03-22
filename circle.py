import math
class Circle: 
    def __init__(self, radius: float): # A class to represent a circle
        self.radius = radius # Initialise Circle with a radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius # Calculate and return the perimeter (circumference) of the circle

    def area(self) -> float:
        return math.pi * self.radius ** 2 # Calculate and return the area of the circle
# 12. Circle class:
# (a) Write a Circle class that holds an instance variable for its center and radius. Provide
# a method to compute the area and a method to compute the perimeter. Make sure that
# the radius cannot be negative.
import math


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = 0 if radius < 0 else radius

    def area(self):
        pi = math.pi
        area = pi * (self.radius ** 2)
        return area

    def circumference(self):
        pi = math.pi
        circumference = 2 * pi * self.radius
        return circumference


circle1 = Circle((0, 0), -10)
print(circle1.area())
print(circle1.circumference())

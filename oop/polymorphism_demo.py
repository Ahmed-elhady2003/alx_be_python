import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override area() method")


class Rectangle(Shape):
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
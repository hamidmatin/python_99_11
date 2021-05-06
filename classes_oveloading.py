import math


class Shape:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def show_area(self):
        print(f"Area is {self.area}")

    def show_perimeter(self):
        print(f"Perimeter is {self.perimeter}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def show_area(self):
        self.area =  self.width * self.height
        super().show_area()
        
    def show_perimeter(self):
        self.perimeter =  2 * (self.width + self.height)
        super().show_perimeter()

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def show_area(self):
        self.area = math.pi * self.radius ** 2
        super().show_area()

    def show_perimeter(self):
        self.perimeter =  2 * math.pi * self.radius
        super().show_perimeter()
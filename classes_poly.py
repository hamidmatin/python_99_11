import math

class Vehicle:
    def __init__(self, model):
        self.model = model

    def show_model(self):
        print(f"Vehicle Model name is {self.model}")


class Bike(Vehicle):
    def show_model(self):
        print(f"Bike Model name is {self.model}")


class Car(Vehicle):
    def show_model(self):
        print(f"Car Model name is {self.model}")


class Aeroplane:
    pass

###################################
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    def area(self):
        print(f"Area of Rectangle is {self.width * self.height}")
    def perimeter(self):
        print(f"Perimeter of Rectangle is {2 * (self.width + self.height)}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(f"Area of Circle is {math.pi * self.radius ** 2}")
    def perimeter(self):
        print(f"Perimeter of Circle is {2 * math.pi * self.radius}")
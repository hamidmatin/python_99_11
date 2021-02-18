# def function_name(parameter_1, parameter_2, …, parameter_n):
#     statement(s)

import math

def area_trapezium(a, b, h):
  area = (a + b) * h * .5
  print(f"Area of a Trapezium is {area}")

def area_circle(radius):
  area = radius ** 2 * math.pi
  return area

a = float(input('Enter a :'))
b = float(input('Enter b :'))
h = float(input('Enter h :'))
area_trapezium(a, b, h)

r = float(input("Enter Radius :"))

c_a = area_circle(r)
print(f"Area of a Circle is {c_a}")
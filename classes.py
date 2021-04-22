import math

#################################################
class Student:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    # print(self)

  def full_name(self):
    return f'{self.first_name} {self.last_name}'

#################################################
class Test:
  def show_message(self, message):
    print(message)

  def set_message(self, message):
    self.message = message

  def get_message(self):
    return self.message

#################################################
class Circle:
  def __init__(self, radious):
    self.radious = radious
  def get_area(self):
    return math.pi ** 2 * self.radious
  def get_mohit(self):
    return math.pi * 2 * self.radious
  def get_arc_length(self, angle):
    return self.get_mohit() * angle / 360

#################################################
class ClassWithPrivate:
  def __init__(self, parameter):
    # if(parameter < 0):
    #   parameter = 0
    parameter = self.__check_value(parameter)

    self.__private_property = parameter

  def get_private_prop(self):
    return self.__private_property
  
  def set_private_prop(self, value):
    # if(value < 0):
    #   value = 0
    value = self.__check_value(value)

    self.__private_property = value

  def __check_value(self, value):
    if(value < 0):
          value = 0
    return value
  
#################################################
class Circle_Private:
  def __init__(self, radious):
    radious = self.__check_value(radious)
    self.__radious = radious

  def get_area(self):
    return math.pi ** 2 * self.__radious

  def get_mohit(self):
    return math.pi * 2 * self.__radious

  def get_arc_length(self, angle):
    return self.get_mohit() * angle / 360
  
  def set_radious(self, radious):
    radious = self.__check_value(radious)
    self.__radious = radious

  def __check_value(self, value):
    if(value < 0):
          value = 0
    return value

###################################
class Course:
  def __init__(self, name, duration):
    self.__name = name
    self.__duration = duration
  
  def get_name(self):
    return self.__name
  
  def get_duration(self):
    return self.__duration

class Teacher:
  def __init__(self, first_name, last_name, course):
    self.__first_name = first_name
    self.__last_name = last_name
    self.course = course
  
  def full_name(self):
    return f'{self.__first_name} {self.__last_name}'
  


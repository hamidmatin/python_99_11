import classess_inheritance
import classes_poly
import classes_oveloading

def shape_type(shape_obj):
  shape_obj.area()
  shape_obj.perimeter()


def main():
  # Start Session 09
  print('Session 9')
  
  c1 = classess_inheritance.BackendCourse('Python', 40)
  c1.show_info()

  t1 = classess_inheritance.Teacher('Hamid Reza', 'Izadi matin', c1)
  t1.show_info()

  silva_book = classess_inheritance.Fiction("Daniel Silva", "Prince of Fire", "Berkley")
  silva_book.invoke_base_class_method()
  silva_book.invoke_self_method()

  silva_book.book_info();
  
  ########## Multiple Inheritance ##########
  print(f"Is Cook a derived class of Poissonier Base Class? {issubclass(classess_inheritance.Cook,(classess_inheritance.Entremetier, classess_inheritance.Poissonier))}")

  chef = classess_inheritance.Cook("SeaFood", "Vegetables")
  chef.invoke_base_class_methods()
  chef.display_chef_info()


  ############ Polymorphism ##############
  ducati = classes_poly.Bike("Ducati-Scrambler")
  beetle = classes_poly.Car("Volkswagon-Beetle")
  boeing = classes_poly.Aeroplane()

  for each_obj in [ducati, beetle, boeing]:
    try:
      each_obj.show_model()
    except:
      print("Expected method not present in the object")

  ####################
  rectangle_obj = classes_poly.Rectangle(10, 20)
  circle_obj = classes_poly.Circle(10)
  for each_obj in [rectangle_obj, circle_obj]:
    shape_type(each_obj)

  #################
  rectangle2_obj = classes_oveloading.Rectangle(10, 20)
  circle2_obj = classes_oveloading.Circle(10)
  rectangle2_obj.show_area()
  rectangle2_obj.show_perimeter()
  circle2_obj.show_area()
  circle2_obj.show_perimeter()

if(__name__ == "__main__"):
  main()

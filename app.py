import classes

def main():
  # Start Session 08
  print('Session 8')
  
  st1 = classes.Student('Navid', 'Azimi')
  st2 = classes.Student('Abolfazl', 'Soltani')
  print(f'{st1.first_name} {st1.last_name}')
  print(f'{st2.first_name} {st2.last_name}')
  print('--------')
  print(st1.full_name())
  print(st2.full_name())

  #############
  obj_test = classes.Test()
  obj_test.show_message('Hello class')
  obj_test.set_message('this is set with set_message method')
  print(obj_test.get_message())


  ######################
  c1 = classes.Circle(10)
  print(f'Area of c1 is : {c1.get_area()}')
  print(f'Mohit of c1 is : {c1.get_mohit()}')
  
  # c1.radious = -20

  print(f'Arc length with 30 deg : {c1.get_arc_length(30)}')
  
  
  ####################### Private properties and methods
  obj_private = classes.ClassWithPrivate(20)
  # print(obj_private.__private_property)
  print(f'pirvate property is : {obj_private.get_private_prop()}')

  obj_private.set_private_prop(-10)
  print(f'pirvate property is : {obj_private.get_private_prop()}')

  ######################
  c2 = classes.Circle_Private(10)
  print(f'Area of c2 is : {c2.get_area()}')
  print(f'Mohit of c2 is : {c2.get_mohit()}')
  
  c2.set_radious(-20)

  print(f'Arc length with 30 deg : {c2.get_arc_length(30)}')


  #####################################
  python_course = classes.Course('Python', 40)
  t1 = classes.Teacher('Hamid reza', 'Izadi Matin', python_course)

  print(t1.full_name())
  print(t1.course.get_name())



if(__name__ == "__main__"):
  main()

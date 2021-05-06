import classess_inheritance

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
  
if(__name__ == "__main__"):
  main()

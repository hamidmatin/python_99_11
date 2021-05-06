class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show_info(self):
        print(f'Course Name: {self.name}, Duration: {self.duration}')


class BackendCourse(Course):
    def get_info(self):
        return f'Course Name: {self.name}, Duration: {self.duration}'


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(Person):
    def __init__(self, first_name, last_name, theaches):
        super().__init__(first_name, last_name)
        self.theaches = theaches

    def show_info(self):
        print(f'{self.full_name()}, Theaches : {self.theaches.get_info()}')


#############
class Book:
  def __init__(self, author, title):
    self.author = author
    self.title = title
  
  def book_info(self):
    print(f"{self.title} is authored by {self.author}")

class Fiction(Book):
  def __init__(self, author, title, publisher):
    super().__init__(author, title)
    self.publisher = publisher
    
  def book_info(self):
    print(f"{self.title} is authored by {self.author} and published by {self.publisher}")

  def invoke_base_class_method(self):
    super().book_info()

  def invoke_self_method(self):
    self.book_info()

########### Multiple Inheritance ###############
class Poissonier:
  def __init__(self, poissonier_role):
    self.poissonier_role = poissonier_role
  
  def display_chef_info(self):
    print(f"Chef is mainly involved in preparing {self.poissonier_role}")
class Entremetier:
  def __init__(self, entremetier_role):
    self.entremetier_role = entremetier_role
  
  def display_chef_info(self):
    print(f"Chef is mainly involved in preparing {self.entremetier_role}")
class Cook(Poissonier, Entremetier):
  def __init__(self, poissonier_role, entremetier_role):
    Poissonier.__init__(self, poissonier_role)
    Entremetier.__init__(self, entremetier_role)
  
  def invoke_base_class_methods(self):
    # self.display_poissonier_chef_info()
    # self.display_entremetier_chef_info()
    Poissonier.display_chef_info(self)
    Entremetier.display_chef_info(self)

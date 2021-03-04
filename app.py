import inner_function_module
import recursive_function
import default_parameter


def function_defination_with_no_argument():
  print("This is a function definition with NO Argument")
  # create local variable 
  my_global = 60

  print(f'My global at f1 is : {my_global}')

def function_defination_with_one_argument(message):
  print(f"This is a function definition with {message}")
  # Use global keyword for change global variable
  global my_global
  my_global = 60

def main():
  print(f'My global at begining is : {my_global}')
  function_defination_with_no_argument()
  print(f'My global after call f1 is : {my_global}')
  function_defination_with_one_argument("One Argument")
  print(f'My global after call f2 is : {my_global}')

  inner_function_module.outer_function()

  # n = int(input('Enter a number : '))
  n = 2
  fac = recursive_function.factorial(n)
  print(f'{n}! = {fac}')

  fac = recursive_function.factorial_rec(n)
  print(f'{n}! = {fac}')

  #####################
  default_parameter.work_area("Alice has interest in", "Internet of Things")
  default_parameter.work_area("Sam works in")
  default_parameter.work_area_2("Sam works in")
  default_parameter.work_area_2("Sam works in", "LA")
  default_parameter.work_area_2("Sam works in", city="LA")
  default_parameter.work_area_2(prompt="Sam works in", domain="Internet of Things", city="LA")
  default_parameter.work_area_2(city="LA", prompt="Sam works in", domain="Internet of Things")

  print('1',end='')
  print('2')
if(__name__ == "__main__"):
  main()
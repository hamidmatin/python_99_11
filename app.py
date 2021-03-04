import inner_function_module
import recursive_function

my_global = 10

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

  n = int(input('Enter a number : '))
  fac = recursive_function.factorial(n)
  print(f'{n}! = {fac}')

  fac = recursive_function.factorial_rec(n)
  print(f'{n}! = {fac}')

if(__name__ == "__main__"):
  main()
import tuples
import sets
import dictionary

def main():
  # Start Session 07
  print('Session 7')
  # tuples.tuple_intro()
  # tuples.tuple_slicing()
  # tuples.tuple_methods()

  # swap variables
  a = 10
  a, b = 20, 30
  print(f'a = {a}, b = {b}')
  
  b, a = a, b
  print(f'a = {a}, b = {b}')
  
  # tuples.multiple_value()

  # ###### SETS ############
  # sets.set_intro()
  # sets.set_methods()


  # ####### DICTIONARY ############
  dictionary.dictionary_intro()
  
if(__name__ == "__main__"):
  main()

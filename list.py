def list_intro():
  # ################ Array (list) ###############
  # list_name = [value, value, value, ....]
  # item 
  # index => position of item in list => zero base
  # lenth or count => count of items in array

  number_list = [10, 20, 30, 50, 12]
  print(number_list)

  string_list = ["Soltani", 'Khadem', "Aghili", "Karimi", "Azimi"]
  print(string_list)

  mixed_list = ['Soltani', 20, True]
  print(mixed_list)

  empty_list = []
  print(empty_list)

  # GET => list[index]
  # index => positive and negative
  # if index is positive => begin to end
  # if index is negative => end to begin

  print(string_list[0])
  print(string_list[1])
  print(string_list[-1])
  print(string_list[-2])

  # Raise list index out of range Error
  # print(string_list[5])
  # print(string_list[-6])
  
def basic_list_operators():
  list_1 = [1, 3, 5, 7]
  list_2 = [2, 4, 6, 8]
  # concat list_1 and list_2 => append list_2 to list_1
  list_3 = list_1 + list_2
  print(list_3)

  print(list_1 * 3)

  # Equal
  print(list_1 == list_2)
  print(list_1 == list_3)
  print(list_3 == [1, 3, 5, 2, 4, 6, 8, 7])

  name = "Mahammad"
  print(name == 'Mohamadm')

  # in operator
  num = 5
  print(num in list_1)
  print(num in list_2)
  print(num in list_3)

  # list()
  quote = "How you doing?"
  string_to_list = list(quote)
  print(string_to_list)

  friends = ["j", "o", "e", "y"]
  # print(friends + quote  )
  print(friends + string_to_list)

def ref_type_vs_value_type():
  a = 10
  b = a

  a = 20
  print(f'a = {a}, b = {b}')

  list_1 = [1, 2, 3, 4]
  list_2 = list_1

  list_1[1] = 200
  print(f'list 1 = {list_1}')
  print(f'list 2 = {list_2}')

  list_2[2] = -150
  print(f'list 1 = {list_1}')
  print(f'list 2 = {list_2}')

  nomreh_list = [80, 60, 95, 100]

  s = sum(nomreh_list.copy())
  print(f'nomarat = {nomreh_list}, sum = {s}')

  # s = sum(nomreh_list)
  # print(f'nomarat = {nomreh_list}, sum = {s}')

  copy_of_nomarat = nomreh_list.copy()
  s = sum(copy_of_nomarat)
  print(f'nomarat = {nomreh_list}, sum = {s}, copy of nomarat = {copy_of_nomarat}')

  result = sum_with_copy(nomreh_list)
  print(f'nomarat = {nomreh_list}, sum = {result[0]}, copy of nomarat = {result[1]}')

  result2 = sum_with_copy(list_1)
  print(f'List 1 = {list_1}, result[0] = {result2[0]}, result[1] = {result2[1]}')

def sum(list):
  sum = 0
  counter = 0
  for number in list:
    sum += number
    list[counter] *= 2
    counter += 1
  return sum

def sum_with_copy(list):
  sum = 0
  copy_list = list.copy()

  counter = 0
  for number in list:
    sum += number
    copy_list[counter] *= 2
    counter += 1
  return [sum, copy_list]

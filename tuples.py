from typing import Tuple


def tuple_intro():
    internets_list = ["cern", "timbernerslee", "www", 1980]
    internets_tuple = ("cern", "timbernerslee", "www", 1980)

    print(internets_list)
    print(internets_tuple)

    print(internets_list[1])
    print(internets_tuple[1])

    front_end = ('html', 'css', 'javascript', internets_tuple)

    print(front_end)

    tuple_1 = (9, 7, 1, 4)
    tuple_2 = (9, 6, 2, 4)
    tuple_3 = tuple_1 + tuple_2

    print(tuple_3)

    internets_list[0] = 'new Value'
    print(internets_list)

    # can not modify items
    # internets_tuple[0] = 'new Value'
    # print(internets_list)

    print(tuple_1 > tuple_2)
    print(tuple_1 == tuple_2)

    # convert string to tuple
    firstName = 'Hamid reza'
    string_to_tuple = tuple(firstName)
    print(string_to_tuple)

    list_to_tuple = tuple(internets_list)
    print(list_to_tuple)

    tuple_to_list = list(internets_tuple)
    print(tuple_to_list)

def tuple_slicing():
    student_tuple = ('karimi', 'khadem', 'azimi', 'aghili')
    student_list = ['karimi', 'khadem', 'azimi', 'aghili']

    print(student_tuple[0])
    print(student_tuple[1])
    print(student_tuple[2:])
    print(student_tuple[:2])

    st1, st2, st3, st4 = student_tuple
    print(f'st1 = {st1}, st2 = {st2}, st3 = {st3}, st4 = {st4}')

    st1_list, st2_list, st3_list, st4_list = student_list
    print(f'st1_list = {st1_list}, st2_list = {st2_list}, st3_list = {st3_list}, st4_list = {st4_list}')

    print("Same as List Slicing")

def tuple_methods():
    student_tuple = ('karimi', 'khadem', 'azimi', 'aghili')
    for student in student_tuple:
        print(student)

    student_tuple_sorted =  sorted(student_tuple)
    print(student_tuple_sorted)

    tuple_1 = (1 , 2)
    tuple_2 = (3 , 4)
    tuple_1 = tuple_1 + tuple_2
    print(tuple_1)

    tuple_3 = (5, 6)
    tuple_1 += tuple_3

    print(tuple_1)

    tuple_items = ()

    for i in range(5):
        num = int(input('Enter a Number :'))
        # tuple_items += (num,) 
        tuple_items += num, 

    print(tuple_items)
    print(tuple_items.count(1))

def return_multiple_items_by_list():
  monument = input("Which is your favorite monument? ")
  year = input("When was it constructed? ")
  return [monument, year]

def return_multiple_items():
  monument = input("Which is your favorite monument? ")
  year = input("When was it constructed? ")
  return monument, year

def multiple_value():
    # ##### Return of Multiple Values from a Function
    answer1 = return_multiple_items_by_list()
    print(f'answer1 = {answer1}')
    # print(f"My favorite monument is '{answer1[0]}' and it was constructed in '{answer1[1]}'")

    c = 10, 20, 30
    print(f'c = {c}')

    mnt, yr = return_multiple_items()
    print(f"My favorite monument is '{mnt}' and it was constructed in '{yr}'")

    answer2 = return_multiple_items()
    print(f"My favorite monument is '{answer2[0]}' and it was constructed in '{answer2[1]}'")


def dictionary_intro():
    students = {
        '001': 'Khadem',
        '002': 'Aghili',
        '003': 'Azimi',
        '004': 'Karimi'
    }

    print(students)

    print(students['003'])

    numbers = dict(one=1, two=2, three=3)
    print(numbers)

    sample = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(sample)

    st1 = {'firstName': 'Arman', 'lastName': 'Khadem'}
    st2 = {'firstName': 'Navid', 'lastName': 'Azimi'}
    st3 = {'firstName': 'Setare', 'lastName': 'Aghili'}
    st4 = {'firstName': 'Sina', 'lastName': 'Karimi'}

    print_student(st2)

    student_dic = {
        1: st1,
        2: st2,
        3: st3,
        4: st4
    }

    # print_student(student_dic[4])

    for student_id in student_dic:
        print(student_dic[student_id])

    for student_id in student_dic:
        print_student(student_dic[student_id])

    print(st1.get('firstName'))
    print(st1['firstName'])

    print(st1.get('age'))
    print(st1.get('age', 30))
    #### Raise Error
    # print(st1['age'])


    print(st1.items())
    newSt1 = st1.items()
    print(newSt1)

    print(st1.keys())

    print(student_dic.pop(2))
    print(student_dic)

def print_student(student):
    print(f"Student : {student['firstName']} {student['lastName']}")

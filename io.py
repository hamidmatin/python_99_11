# variable_name = input([prompt])
first_name = input('Enter your Name: ')
last_name = input('Enter your Lastname: ')

full_name = first_name + ' ' + last_name

print('Hello', full_name)
print('Hello', first_name, last_name)
print('Hello', first_name, last_name, sep=None)
print('Hello', first_name, last_name, sep="*")
print('Hello', first_name, last_name, sep="*", end="--->")
print('Hello {0} {1}'.format(first_name, last_name))
print('Hello {1} {0}'.format(first_name, last_name))
print('Hello {0} {0}'.format(first_name, last_name))

message = 'Hello {0} {1}'

print(message.format(first_name, last_name))

city = input('City : ')
street = input('Street : ')
zip = input('Zip : ')
phone = input('Phone : ')

address = '''
   City: {city}
   Street: {street}
   Zipcode: {zip}
   Phone: {phone}
'''

print(address.format(city='Tehran', street='ksgdhsg', zip='2554545', phone='45456'))
print(address.format(street='ksgdhsg', city='Tehran', zip='2554545', phone='45456'))

print(f'''
   City: {city}
   Street: {street}
   Zipcode: {zip}
   Phone: {phone}
''')
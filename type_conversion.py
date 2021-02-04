input_radius = input("Enter the radius of a circle : ")

# radius = int(input_radius)
radius = float(input_radius)

circle_area = radius ** 2 * 3.14

print(circle_area)

# prompt = f'Area is {circle_area}' 
prompt = 'Area is ' + str(circle_area)

print(prompt)

print(chr(9556), chr(9552) * 50, chr(9559), sep='')
print(chr(0x2554), chr(0x2550) * 50, chr(0x2557), sep='')

print(ord("Z"))
print(ord("z"))
print(ord("ب"))

print('Hexadecial num', 0x10)
print('Octal num', 0o10)
print('decimal num', 10)

print('Hexadecimal number of 16', hex(16))
print('Octal number of 8', oct(8))
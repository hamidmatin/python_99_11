# Operators
# x + y
# operand operator operand
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Bitwise Operators

print('Arithmetic Operators')
x = 5
y = 3

result = x + y + 3 + 6
print(result)

result = x - y
print(result)

result = x / y
print(result)

result = x * y
print(result)

result = x ** y
print(result)

result = x % y
print(result)

result = x // y
print(result)

# 1. **
# 2. * , / , %, // =>  left to right
# 3. + , - left to right

result = x + 6 * 3 - y ** 2
# (1) = y ** 2 = 9
# (2) = 6 * 3 = 18
# (3) = x + (2) = 5 + 18 = 23
# (4) = (3) - (1) = 23 - 9 = 14
print(result)

result = ((x + 6) * (3 - y)) ** 2
print(result)

# Start Session 2
student_first_name = 'Mohammad'
student_last_name = 'Azimi'
student_full_name = student_first_name + ' ' + student_last_name

print(student_full_name)

print('Rad' * 5)

################ 2. Assignment Operators
# variable = literal or expression#
# = Assignment
# += Addition Assignment


print('Assignment Operators')
a = 10
b = 20
c = a + b

c = c + 5
print(c)

c += 5          # c = c + 5
c -= 5          # c = c - 5
c *= 5          # c = c * 5
c /= 5          # c = c / 5
c //= 5         # c = c // 5
c %= 5          # c = c % 5
c **= 5         # c = c ** 5
c += 1          # c = c + 1 => c++ doesn’t support
c -= 1          # c = c - 1 => c-- doesn’t support

################ 3. Comparison Operators
# value comparision value  => bool => True or False

print('Comparison Operators')

x = 20
y = 20

print(x == y)
print(x != y)

x = 15
print(x == y)
print(x != y)
print(x > y)
y = 15
print(x < y)
print(x >= y)
print(x <= y)

print('"Aston" > "Asher"', "Aston" > "Asher", sep=" = ")
print('"Aston" > "aston" = ', "Aston" > "aston")

# Logical Operators
# bool logical bool => bool
# and   or   not

print('Logical Operators')

print('True and True = ', True and True)
print('True and False = ', True and False)
print('False and True = ', False and True)
print('False and False = ', False and False)

print('-------')
print('True or True = ', True or True)
print('True or False = ', True or False)
print('False or True = ', False or True)
print('False or False = ', False or False)

print('-------')
print('not True = ', not True)
print('not False = ', not False)

############ Bitwise Operators

print('Bitwise Operators') 

print(65 & 98)
print(65 | 98)
print(5 * -x)
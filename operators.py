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

# 2. Assignment Operators
# variable = literal or expression#
# = Assignment
# += Addition Assignment
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


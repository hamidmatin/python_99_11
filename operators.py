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
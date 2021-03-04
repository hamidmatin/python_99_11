def factorial(number):
  result = 1
  if number < 1 :
    return 0
  elif number == 1:
    return 1
  else:
    for n in range(2, number + 1):
      result *= n
    return result


def factorial_rec(number):
  if number == 1:
    return 1
  else:
    result = number *  factorial_rec(number - 1)
    return result
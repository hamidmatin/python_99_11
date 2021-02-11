number = int(input('Enter a number : '))

factorial = 1

if number < 0:
  print("Factorial doesn't exist for negative numbers")
else:
  if number > 0:
    for i in range(2, number + 1):
      factorial *= i
  print(f"The factorial of number {number} is {factorial}")6
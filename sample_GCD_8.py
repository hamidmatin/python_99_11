m = int(input("Enter first positive number : "))
n = int(input("Enter second positive number : "))
if m == 0 and n == 0:
  print("Invalid Input")
else :
  if m == 0:
    print(f"GCD is {n}")
  elif n == 0:
    print(f"GCD is {m}")
  else:
    while m != n:
      if m > n:
        m = m - n
      if n > m:
        n = n - m
    print(f"GCD of two numbers is {m}")
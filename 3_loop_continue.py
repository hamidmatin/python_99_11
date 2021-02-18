start = int(input('Enter a number for start : '))
end = int(input('Enter a number for end : '))

for i in range(start, end):
  if(i % 3 == 0):
    continue

  print(f'Number is :{i}')
score = int(input("Enter your score : "))
grade = ''

if score < 0 or score > 100:
  print('Wrong Number')
else:
  if score >= 90:
    grade = 'A'
  elif score >= 80:
    grade = 'B'
  elif score >= 70:
    grade = 'C'
  elif score >= 60:
    grade = 'D'
  else:
    grade = 'F'

  print(f'Your Grade is "{grade}"')
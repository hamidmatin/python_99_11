i = 0
while i < 5:
  print(f'Number {i}')
  i += 1

print('finished')

score = 0
score_sum = 0
count = -1
while score >= 0:
  score_sum += score
  count += 1
  score = int(input('Enter score (-1 for end) : '))

print(f'Sum of score is {score_sum}, and average is {score_sum / count}')
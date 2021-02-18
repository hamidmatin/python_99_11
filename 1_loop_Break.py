score = 0
score_sum = 0
count = 0
while True:
  score = int(input('Enter score (-1 for end) : '))
  if score < 0:
    break
  score_sum += score
  count += 1
  if count >= 10:
    break
  
print(f'Sum of score is {score_sum}, and average is {score_sum / count}')
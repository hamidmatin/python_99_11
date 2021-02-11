day_num = int(input('Enter day number (0-6) : '))
day = ''
if day_num == 0:
  day = 'Sunday'
elif day_num == 1:
  day = 'Monday'
elif day_num == 2:
  day = 'Tuesday'
elif day_num == 3:
  day = 'Wednsday'
elif day_num == 4:
  day = 'Thursday'
elif day_num == 5:
  day = 'Friday'
else:
  day = 'Saturday'

print(f'Today is {day}')


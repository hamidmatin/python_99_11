day_num = int(input('Enter day number (0-6) : '))
day = ''
if day_num == 0:
  day = 'Sunday'
if day_num == 1:
  day = 'Monday'
if day_num == 2:
  day = 'Tuesday'
if day_num == 3:
  day = 'Wednsday'
if day_num == 4:
  day = 'Thursday'
if day_num == 5:
  day = 'Friday'
if day_num == 6:
  day = 'Saturday'

print(f'Today is {day}')
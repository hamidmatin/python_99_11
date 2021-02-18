command = ''
is_started = False

while True:
  command = input('Enter a command (? for help) > ').lower()
  
  if command == '?':
    print('''
start => for start 
stop => for stop
quit => for quit
    ''')
    
  elif command == 'start':
    if not is_started:
      print('Motor is Starting')
      is_started = True
    else:
      print('Motor is already Started')
  elif command == 'stop':
    if is_started:
      print('Motor is Stoping')
      is_started = False
    else:
      print('Motor is already Stoped')
  elif command == 'quit':
    if is_started:
      print('Motor must be Stop')
    else:
      break
  else:
    print('Unknown command')
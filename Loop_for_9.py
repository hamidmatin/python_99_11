# range([start ,] stop [, step])
# start → value indicates the beginning of the sequence. 
#         If the start argument is not specified, 
#         then the sequence of numbers start from zero by default.
#       
# stop → Generates numbers up to this value but not including the number itself. 
# 
# step → indicates the difference between every two consecutive numbers in 
#        thesequence. The step value can be both negative and positive 
#        but not zero.
# range(5) => 0,1,2,3,4 
# range(4, 8) => 4,5,6,7
# range(8, 4, -1) => 8,7,6,5
# range(4, 10, 2) => 4, 6, 8

# for iteration_variable in sequence:
#   statement(s)

for i in range(5):
  print(i, end=', ')

print('')
for i in range(4, 8):
  print(i, end=', ')

print('')
for i in range(8, 4, -1):
  print(i, end=', ')

print('')
for i in range(4, 10, 2):
  print(i, end=', ')
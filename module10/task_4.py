print('Задача 4. Крест')

# Напишите программу,
# которая выводит на экран крест из символов “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)

# ^        ^
#  ^      ^ 
#   ^    ^  
#    ^  ^   
#     ^^    
#     ^^    
#    ^  ^   
#   ^    ^  
#  ^      ^ 
# ^        ^

x = int(input('Введите размер стороны квадрата: '))
print()                      # воображаемый квадрат
for row in range(x):
  for col in range(x):
    if col == row:
      print('^', end = ' ')
    elif col == -row + (x-1):
      print('^', end = ' ')
    else:
      print(' ', end = ' ')
  print()

print()
x = int(input('Введите размер стороны: '))
print()
for row in range(x):
  for col in range(x):
    if col == row:
      print('^', end = '')
    elif col == -row + x-1:
      print('^', end = '')
    else:
      print('', end = ' ')
  print()

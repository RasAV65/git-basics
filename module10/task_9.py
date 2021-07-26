print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

print() #вариант 1
size = int(input('Введите высоту пирамиды: '))
print()
number = 1
for row in range(size):
  for col in range(size - row - 1):
    print(end = '\t')
  for col in range(row + 1):
    print(number, end = '\t\t')
    number += 2
  print()

print() #вариант 2
rows = int(input('Введите высоту пирамиды: '))
print()
new_num = 1
for line in range(rows):
  space_count = rows - line - 1
  print('\t' * space_count, end = '')
  for number in range(line + 1):
    print(new_num, end = '\t\t') # из разбора ДЗ использует пробелы, что не дает ровного отображения, поэтому \t
    new_num += 2
  print()


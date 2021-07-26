print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

print() #вариант 1
x = int(input('Введите глубину ямы: '))
for row in range(x, 0, -1):
  for col in range(x, 0, -1):
    if col >= row:
      print(col, end = '')
  for i in range(1, x + 1):
    if i >= row:
      print(i, end = '')
    else:
      print('..', end = '')
  print()

print() #вариант 2
depth = int(input('Введите глубину ямы: '))
for line in range(depth):
  for left_number in range(depth, depth - line - 1, -1):
    print(left_number, end = '')
  point_count = 2 * (depth - line - 1)
  print('.' * point_count, end = '')
  for right_number in range(depth - line, depth + 1):
    print(right_number, end = '')
  print()

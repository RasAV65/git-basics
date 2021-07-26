print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print()
size = int(input('Введите число: '))
for row in range(1, size + 1):
  for col in range(size):
    if col < row:
      print(row, end = ' ')
  print()

print()
size = int(input('Введите число: '))
for row in range(1, size + 1):
  for col in range(size):
    if col < row:
      print(row, end = '\t') # для более ровного отображения если > 9
  print()

print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15

def summ():
  N = int(input('Введите число: '))
  summ = 0
  for num in range(1, N + 1):
    summ += num
  print('Я знаю, что сумма чисел от', 1, 'до', N, 'равна', summ)

summ()

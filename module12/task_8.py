print('Задача 8. НОД')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел

# делим
def nod():
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  while a != 0 and b != 0:
    if a > b:
      a = a % b
    else:
      b = b % a
  c = a + b
  print(c)

nod()

# вычитаем
def nod():
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a        
  print(a)

nod()

# math
import math
def nod():
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  print(math.gcd(a, b))

nod()

# math
# с аргументами (они же параметры)
#import math
def nod(c, d): # в скобках переменные
  print(math.gcd(c, d)) # в скобках используемые (объявленные) переменные

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

nod(a, b) # в скобках аргументы!


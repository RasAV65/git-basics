print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

print()
def f(n):
  factorial = 1
  while n > 1:
    factorial *= n
    n -= 1
  return factorial

precision = float(input('Введите точность: '))
x = int(input('Введите x: '))
addMember = 1
result = 0

y = 0

while abs(addMember) > precision:
  addMember = pow(-1, y) * (pow(x, (2 * y)) / f((2 * y)))
  result += addMember
  y += 1
print('Сумма ряда =', result)


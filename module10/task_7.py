print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

print()
seqNum = int(input('Сколько будет чисел: '))
temp = 0
full = 0
maxfull = 0
summ = 0
numCount = 0

for num in range(seqNum):
  print('Введите', num, 'число: ', end = '')
  number = int(input())
  while number != 0:
    full = number
    while number > 0:
      temp = number % 10
      numCount += temp
      number //= 10
      if summ < numCount:
        summ = numCount
        maxfull = full
    numCount = 0

print('Число', maxfull, 'имеет максимальную сумму цифр:', summ)

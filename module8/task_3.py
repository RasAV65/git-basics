print('Задача 3. Это будет бомба')

# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
# 
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва.. 
# 
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.

n = int(input('Введите кол-во секунд: '))
for num in range (n - 1, -1, -1):
  bomb = int(input('Обезвредить бомбу сейчас? '))
  if bomb == 0:
    print('Осталось секнд', num)
  elif bomb == 1:
    print('Бомба обезврежена, секунд до взрыва оставалось', num)
    break
if num == 0:
  print('Бомба взорвалась!')

print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».

print('Первый способ')
job = int(input('Введите время работы отделения: '))

if (job >= 8 and job <= 9) or (job >= 12 and job <= 13) or (job >= 15 and job <= 17) or (job >= 20 and job <= 22):
  print('Можно получить посылку')

else:
  print('Посылку получить нельзя')

print()
print('Второй способ')
job = int(input('Введите время работы отделения: '))
if (job >=0 and job <= 7) or (job >=10 and job <=11) or (job == 14) or (job >= 18 and job <= 19) or (job == 23):
  print('Посылку получить нельзя')
else:
  print('Можно получить посылку')

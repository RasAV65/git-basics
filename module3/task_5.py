print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.

minutes = int(input('Количество минут: '))
hour = minutes // 60
minutes_remaining = minutes % 60
print('В часах: ', hour)
print('Минут осталось: ', minutes_remaining)

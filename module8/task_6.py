print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

a = int(input('Сторона квадрата равна: '))
b = 12
c = 0
for num in range(a):
  if a > b:
    a /= 2
    c += 2
print('Свернуть нужно в', c, 'раза')

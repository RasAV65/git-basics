print('Задача 2. Финансовый отчёт')

# Наде дали задание сформировать финансовый отчёт за последние 20 лет по полугодиям. 
# Нужно сумму дохода первых двух кварталов поделить на сумму последних двух кварталов, 
# чтобы понять динамику роста или падения дохода. И так за каждый год. 
# 
# Надя решила, 
# что быстрее будет написать простую программу, которая сделает всё за неё.
# 
# 
# Запросите у пользователя четыре числа.
# Отдельно сложите первые два и отдельно вторые два.
# Разделите первую сумму на вторую.
# Выведите результат на экран.
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвёртое число: '))
e = (a + b) / (c + d)
print('Ответ =', e)

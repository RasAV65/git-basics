print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
print()
print('1-й вариант')
educational_grant = int(input('Ежемесячная стипендия: '))
expenses = int(input('Расходы в первый месяц, со второго +3%: '))
a = educational_grant
b = expenses
for months in range(2, 11):
  expenses = expenses + expenses / 100 * 3
  a += educational_grant
  b += expenses
  b = int(100 * b) / 100
print('Расходы с % составили:', b, 'руб.')
c = b - a
c = int(100 * c) / 100
print('Степендия за 10 месяцев составила', a, 'руб., предстоит уговорить родителей на', c, 'руб.')

print()
print('2-й вариант')
educational_grant = int(input('Ежемесячная стипендия: '))
expenses = int(input('Расходы в первый месяц, со второго +3%: '))
parent = int(input('Сколько дали родители на 10 месяцев: '))
a = educational_grant + parent
b = expenses
for months in range(2, 11):
  print('Месяцев прошло', months)
  expenses = expenses + expenses / 100 * 3
  a += educational_grant
  b += expenses
  b = int(100 * b) / 100
  print('Расходы с % включая этот месяц составили:', b, 'руб.')
if b > a:
  print('Денег не хватило! У вас', a, 'руб., но общие расходы:', b, 'руб.')
else:
  print('У вас', a, 'руб., денег на учебу хватает!')


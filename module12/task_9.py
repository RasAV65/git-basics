print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришли, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
  x = 1 # всегда камень
  a = int(input('Выберите вариант: 1 - камень, 2 - ножницы, 3 - бумага: '))
  if x == a:
    print('Ничья')
  elif x == a - 1:
    print('Вы проиграли')
  elif x == a - 2:
    print('Вы выиграли!')
  else:
    print('Выберите варианты от 1 до 3')
    rock_paper_scissors()
  mainMenu()

def guess_the_number():
  print()
  b = 266
  num = int(input('Угадайте число \nПодсказка - действующий Папа: '))
  if num == b:
    print('Угадали!')
    input('Нажмите любую кнопку чтобы вернуться в меню.') 
    mainMenu()
  else:
    input('Не угадали, попробуйте еще раз. \nДля продолжения нажмите Enter..')
    guess_the_number()

def mainMenu():
  print()
  print('Выберите игру: ')
  choice = int(input('1 - игра "Камень, ножницы, бумага", \n2 - игра "Угадай число"\n'))
  if choice == 1:
    rock_paper_scissors()
  if choice == 2:
    guess_the_number()
  else:
    print('Выберите варианты 1 или 2')
    mainMenu()

mainMenu()
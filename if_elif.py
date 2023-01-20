#if = если
#elif = иначе,если
#else = иначе


#a = 40
#b = 20
#c = 10


#if a > b:
#    print(True)
#elif a < b:
#    print(False)

#if a == b:
#    print(False)
#elif a > c:
#    print(True)


#lang = input('Выберите язык: EN RU KG: ')
#if lang == 'EN' :
#    print('Hello')
#elif lang == 'RU' : 
#    print('Привет')
#elif lang == 'KG':
#    print('Салам')
#else:
#    print('Такого языка нет!') 


#b = 3 ** 2
#a = 2 ** 4

#if a > b:
#    print('a > b')
#elif b > a:
#    print('b > a')
#else:
#    print('b > a')



#age = int(input('Введите ваш возраст: '))
#if age >= 18:
#    print('Вы можете войти, вам', age, 'лет')
#elif age < 18 and age > 12:
#    print('Вы подросток, вам нельзя вам', age, 'лет')
#elif age < 0 or age == 0:
#    print('Что ты такое')
#else:
#    print('Ты ребенок тебе', age, 'лет')


#login = input ('Введите ваш логин: ')
#password1 = int(input('Введите пароль: '))
#password2 = int(input('Повторите пароль: '))

#if password1 == password2:
#    print('Ваш логин: ', login, 'Ваш пароль:', password1)
#else:
#    print('Пароль не верный')



#num1 = int(input('Enter number 1: '))
#num2 = int(input('Enter number 2: '))

#if num1 == num2:
#    print('Числа равны', num1, '=', num2)
#elif num1 > num2:
#    print(num1, '>', num2)
#elif num1 < num2:
#    print(num1, '<', num2)

#num1 = int(input('Введи число: '))
#a = 2
#if num1 == a:
#    print(a * num1)
#elif num1 == 3:
#    print(a * num1)
#elif num1 == 4:
#    print(a * num1)
#else:
#    print('no')




#a = 5
#b = 3
#if a < b:
#    print(True)
#else:
#    print(False)


#a = input ('Выберите действие: + - / *: ')
#num1 = int(input('Введи число: '))
#num2 = int(input('Введи второе число: '))

#if a == '+':
#    print(num1 + num2)
#elif a == '-':
#    print(num1 - num2)
#elif a == '/':
#    print(num1 / num2)
#elif a == '*':
#    print(num1 * num2)

#else:
#    print('Такого действия нет ')


# a = 10
# b = 10
# c = 10
# if a > c and b > c :
#    print('ok')
# else:
#    print('not ok')

#a = 10
#b = 10
#c = 25

#if a > c or b > c:
#    print(True)
#else:
#    print(False)



#b = 8
#if b % 2 == 0:
#    print('Четное число')
#else:
#    print('Не четное число')




# transport = input('какой транспорт вы выбираете: самолет,поезд,автобус: ')

# if transport == 'самолет':
#     ticket_type = input('Каким классом вы хотите лететь: эконом,бизнес: ')
#     if ticket_type == 'эконом':
#         place = input ('Где бы вы хотели сидеть :у окна,в проходе: ')
#     else:
#         place = 'у вас бизнес зал' 


# elif transport == 'поезд':
#     ticket_type = input('Как вы хотите ехать : купе, плацкарт:')
#     if ticket_type == 'купе':
#         place = input('Выберите одно из свободных мест : 12 , 55, 77')
#     elif ticket_type == 'плацкарт':
#         print('В плацкарте мест не осталось!')
#         exit ()


# elif transport == 'автобус':
#     ticket_type = input('Как вы хотите поехать: сидя, стоя')
#     if ticket_type == 'сидя':
#         place = input('Выберите место: 5, 6, 7')

#     else:
#         place = 'Где угодно'
# else:
#     print('Такого транспорта нет')
#     exit()


# print('Ok, вынесите оплату')
# print(f'Вы выбрали: {transport} ваше место: {place}')





#fastfood = input('Что закажете: шаурма, самсы, пирожок: ')

#if fastfood == 'самсы':
#    filling_type = input('Какую начинку хотите: мясо, курица, сыр: ')
#   if filling_type == 'сыр':
#        answer = input('Самсы с сыром закончились,будете ждать: да , нет:')
#       if answer == 'нет':
#           print('Пока')
#           exit()



#elif fastfood == 'самсы':
#   filling_type = input('Какую начинку хотите: мясо, курица, сыр: ')
#    if filling_type == 'сыр':
#        answer = input('Шаурма с сыром закончились,будете ждать: да , нет:')
#if answer == 'да':  
#   answer = input('Сколько хотите:')
#    answer = input('Нужно ли разогреть: да, нет: ')
#    answer = input('Что будете пить: чай, кофе, минералка:')
    

#else:
#    print('Такого блюда нет!')
#    exit()


#print(f'Вы заказали:{fastfood}, {filling_type}, клиент напиток не взял')
#print('Приятного аппетита!')
        



#fastfood = 'Что хотите заказать: шаурма, самсы, пирожок: '
#if fastfood == 'шаурма':
#    filling_type = input("Какую начинку хотите: сыр, курица, мясо": )
#    if filling_type == 'курица':
#        answer = input("Шаурма с курицей не соталось,будете ждать 10 мин?: ")
#    if answer == 'нет':
#        print(Пока)
#        exit()











    

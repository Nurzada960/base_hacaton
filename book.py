
#Нурзада суббота, 7- января начала читать книгу 
#print('Welcome to study!')

#ПЕРЕМЕННЫЕ
#print('Hello Python interpreter!')
#print('hello world!')

# message = "Hello Python world!"
# print(message)

# message = 'Hello Python Crash Course world!'
# print(message)


# n1 = 'Nurzada smart!'
# print(n1)

#STRINGS
# 'This is a string.'
# "This is also string."
# 'I told my friend, "python is my favorite languege!"'
# "The lahguage 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."

# name = 'ada lovelace'
# print(name.title())

#name = 'Ada LoveLace'
#print(name.uppper())
#print(name.lower())

#ПЕРЕМЕННЫЕ В СТРОКАХ
# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'{first_name} {last_name}'
# print(full_name)

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'{first_name} {last_name}'
# print(f'Hello,{full_name.title()}!')

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'{first_name} {last_name}'
# message = f'Hello, {full_name.title()}!'
# print(message)

#ТАБУЛЯЦИИ И РАЗРЫВЫ СТРОК 
#print('Languages:\nPython\nC\nJava')

#УДАЛЕНИЕ ПРОПУСКОВ
# favorite_language = 'python '
# favorite_language = favorite_language.strip()
# favorite_language
# 'python'
# print(favorite_language)

# name = 'Eric'
# num1 = f'Hello, {name}, would you like to learn some Python today!'
# print(num1)

#name = 'eric'
#print(name.lower())
#print(name.upper())
#print(name.title())

# n2 = 'A person who never made a mistake never tried anything new.'
# n3 = f'Albert Einstein once said,"{n2}"'
# print(n3)

# n2 = 'A person who never made a mistake never tried anything'
# famous_person = 'Albert Einstein'
# message = f'{famous_person} once said, "{n2}"'
# print(message)

#ЧИСЛА
#ЦЕЛЫЕ ЧИСЛА

#** возведение в степень
#круглые скобки используюся для изменнения следований операций,чтобы выражение могло выччисляться в нужном порядке.
#2 +3*4
#14
#(2 + 3) * 4
#20


#ВЕЩЕСТВЕННЫЕ ЧИСЛА , ЧИСЛА С ПЛАВАЮЩЕЙ ТОЧКОЙ 
# 0.1 + 0.1
# 0.2

#4/2
#2.0

#1 + 2.0
#3.0

# universe_age = 14_000_000
# print(universe_age)

#mnojstva prisvaivani
# x, y, z = 1, 2, 3
# print(x,y,z)

#kostanta
#neizmennoe znachenie navsegda

# print(5 +3)
# print(9 - 1)
# print(8 * 1)
# print(16 / 2)


# n = 4
# print(n)

#SPISOK

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# bicycles = ['trek', 'cannondalr', 'redline', 'specialized']
# print(bicycles[0])


# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0].title()) 

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1])
# print(bicycles[3])

# bicycles = ['trek', 'cannodale', 'redline', 'speciallized']
# print(bicycles[-1]) 




# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f'My first bicycle was a {bicycles[0].title()}'
# print(message)


# names = ['aiza', 'rauzat', 'kanykei']
# print(names[0])
# print(names[1])
# print(names[2]) 

# names = ['aiza', 'rauzat', 'kanykei']
# message = f'My friend is, {names[0].title()}' 
# message = f'My friend is, {names[1].title()}'
# message = f'My friend is, {names[2].title()}'
# print(message)


# cars =['merc', 'porsch', 'bmw']
# message1 = f'Я хотел бы купить, {cars[0].title()}'
# print(message1) 


#ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ В СПИСКЕ
# motorcycles = ['honda', 'yamaha', 'suzuki']
# #print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)



# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
# print(motorcycles)


# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles) 


#vstavka
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

#udalenie
# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]
# print(motorcycles)

#pop
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)  
# popped_motocycle = motorcycles.pop()           #хранится удаленное значение
# print(motorcycles)                             #показывает что значениебыло удалено
# print(popped_motocycle)                        #удаленное из списка значение остается доступным



#example
# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print(f'The last motorcycle i owned was a {last_owned.title()}.')


# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f'The first motorcycle i owned was a {first_owned.title()}.')



#udalenie po znacheniyu
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles = 'ducati'
# #print(motorcycles)
# too_expensive = 'ducati'
# #motorcycles.remove(too_expensive)
# #print(motorcycles)
# print(f'\nA {too_expensive.title()} is too expensive for me.')

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz']
# invite = (f"Дорогая,{guests[0].title()} приглашаю на ужин.")
# print(invite)

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz']
# invite = (f'Дорогая, {guests[1].title()} приглашаю на ужин')
# print(invite)

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz']
# invite = (f'Дорогая, {guests[2].title()} приглашаю на ужин')
# print(invite)

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz']
# invite = (f'Дорогая, {guests[3].title()} приглашаю на ужин')
# print(invite)


# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz']
# print(guests)
# didnt_come = 'nurkyz'
# guests.remove(didnt_come)
# print(guests)
# guests.insert(3,'marina')
# print(guests)

# guests = ['aiza', 'rauzar', 'kanykei', 'marina']
# invite = f'Приглашаю, {guests[3].title()} на ужин'
# print(invite)

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz', 'marina']
# # print(guests)
# # guests.insert(0,'karina')
# # guests.insert(2,'kanykei')
# guests.append('sasha')
# #print(guests)
# # invite = f'Приглашаю, {guests[4].title()} вас на ужин'
# # print(invite)
# invite = f'Приглашаю, {guests[5].title()} вас на ужин'
# print(invite)

# guests = ['aiza', 'rauzat', 'kanykei', 'nurkyz', 'marina']
# print(guests)
# invite = f'Приглашаю, {guests} только 2 гостя'
# print(invite)
# guests.pop()
# invite = f'Сожалею, {guests[3].title()} нет стула'
# print(invite)
# guests.pop()
# invite = f'Сожалею, {guests[2].title()} нет стула'
# print(invite)
# guests.pop()
# print(guests)
# invite2 = f'Приходите, {guests[0]} жду'
# print(invite2)
# invite2 = f'Приходи {guests[1]} жду'
# print(invite2)
# del guests[0]
# print(guests)
# del guests[0]
# print(guests)



# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
#cars.sort(reverse=True)
#print(cars)
# print('Here is the original list:')
# print(cars)
# print('\nHere is the sorted list:')
# print(sorted(cars))
# print('\nHere is the original list again')
# print(cars)
#ВЫВОД СПИСКА В ОБРАТНОМ ПОРЯДКЕ
# cars.reverse()
# print(cars)


#ОПРЕДЕЛЕНИЕ ДЛИНЫ СПИСКА

# cars = ['bmw', 'audi', 'toyota', 'subaru', 'merc']
# len(cars)

# countries = ['america', 'dushambe', 'bali', 'westcoast', 'france']
# print(countries)
# print(sorted(countries))
# print(countries)
# print(sorted(countries))
# countries.sort(reverse=True)
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# countries.reverse()
# print(countries)
# countries.sort(reverse=True)
# countries.sort()
# print(countries)



#РАБОТА СО СПИСКАМИ
# magicians = ['alice', 'david', 'caroline']
# for i in magicians:
#     print(f'{i.title()}, that was a great trick!')
#     print(f'I cant wait to see your next trick, {i.title()}.\n')
# print('Thank you, everyone. That was a great magic show!')


# magicians = ['alice', 'david', 'carolina']
# for i in magicians:
#     print(i.title() + ',that was a great trick!')
# print(f'I cant wait to see your next trick, {i.title()}.\n')


# pizzas = ['peperoni', 'margarita', 'cheese']
# for i in pizzas:
#     print(f'I like {i.title()} pizza')
#     print(f'Engoy your {i.title()} pizza.\n')
# print(f'BYE!')

# animals = ['tiger', 'begemot', 'jiraf']
# for i in animals:
#     print(f'A {i.title()} wild animal.\n')
# print('Any wild animal is kind!')


#CHISLOVYE SPISKI

# for i in range(1,6):
#     print(i)
# for i in range(6):
#     print(i)
# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# squares = []
# for i in range (1,11):
#     square = i**2
#     squares.append(square)

# print(squares)

# squares = []
# for i in range (1,11):
#     squares.append(i**2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# sum(digits)

# squares = [i**2 for i in range(1,11)]
# print(squares)

# for i in range(1,21):
#     print(i)

# for i in range(2,21,2):
#     print(i)


# for i in range (3,31,3):
#     print(i)


# cub = [2**3 for i in range (1,10)]
# print(cub)

#SLICES
#squares = []


# cub = [2**3 for i in range (1,10)]
# print(cub)

# players = ['charls', 'martine', 'michael', 'florence', 'eli']
# #print(players[-3:])
# print('Here are the first three players on my team:')
# for i in players[:3]:
#     print(i.title())


# my_foods = ['pizza','pasta','lagman']
# friend_foods = my_foods[:]

# my_foods.append('plov')
# friend_foods.append('mank')

# print('My fav foods are: ')
# print(my_foods)

# print('\nMy friends fav foods are: ')
# print(friend_foods)


# players = ['charls', 'martine', 'michael', 'florence', 'eli']
# print('The first three items in the list are : ')
# for i in players[:3:1]:
#     print(i.title())

# players = ['charls', 'martine', 'michael', 'florence', 'eli']
# print('Three items from the middle of the list are : ')
# for i in players[2:4]:
#     print(i.title())

# players = ['charls', 'martine', 'michael', 'florence', 'eli']
# print('The last three items in the list are : ')
# for i in players[-3:]:
#     print(i.title())




# my_pizzas = ['marg', 'pepp', 'cheese']
# friend_pizzas = my_pizzas[:]
# my_pizzas.append('kolb \n')
# print('My fav pizza: ')
# for i in my_pizzas:
#     print(i)




# friend_pizzas.append('syr')
# print('My frien fav pizza: ')
# for i in friend_pizzas:
#     print(i)



#KORTEJI tuples

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200, 50)
# for i in dimensions:
#     print(i)


# dimensions = (200, 50)
# print('Original dimensions: ')
# for i in dimensions:
#     print(i)


# dimensions = (400, 100)
# print('\nModified dimensions: ')
# for i in dimensions:
#     print(i)




# #IF 
# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for i in cars:
#     if i == 'bmw':
#         print(i.upper())
#     else:
#         print(i.title())


# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')

# answer = 17

# if answer != 42:
#     print('That is not the correct answer. Please try again!')


# age_0 = 22
# age_1 = 18
# age_0 >= 21 or age_1 >= 21
# print(True)
# age_0 = 18
# age_0 >= 21 or age_1 >= 21
# print(False)


# dream = 'fly'
# print("If my == 'fly'? I got it !.")
# print(dream == 'fly')

# print('\nIs dream == "swim"? I dont!')
# print(dream == 'swim')

# sasha = 'love'
# print('If sasha = "love" i knew it')
# print(sasha == 'love')

# print('\nIf sasha == "like" no!')
# print(sasha == 'like')


# sasha = 'invite'
# print("If sasha = 'invite' love it ")
# print(sasha == 'invite')

# print("\nIf he will = 'run' sad!!!!")
# print(sasha == 'run')



# day = 'sunny'
# print('If today = "sunny" i will walk')
# print(day == 'sunny')

# print("\nIf will = 'Rain' i will not")
# print(day == 'rain')


# work = "easy"
# print('if my work = "easy" nice')
# print(work == 'easy')

# print('if will not work = "hard" sad')
# print(work == "hard")



# a = 22 
# b = 18
# if a >= 21:
#     print(True)
#     if b >= 21:
#         print(False)

# a = 'Dream'
# if a.lower() == 'dream':
#     print(a == 'Dream')

# goal = ('learn', 'listen', 'watch')
# a = 'read'
# if a not in goal:
#     print(f'please {a} add!')


# boy = ['kind', 'rich', 'clever']
# if 'clever' in boy:
#     print(True)

#     if 'smart' in boy:
#         print(False)




# girl = ('good', 'smart')
# b = 'clever'
# if b not in girl:
#     print(f'Please be a {b} girl!!!')

# a = 22
# b = 22
# if a >= 21 and b >= 21:
#     print(True)
#     if a >= 21 and b >= 21:
#         print(False)


# age = 19
# if age >= 18:
#     print('You are old enough to vote')
#     print('Have you registered to vote yet?')


# age = 18
# if age >= 18:
#     print('Yo are old enough to vote!')
#     print('Have you registered to vote yet?')
# else:
#     print('Sorry, you are too young to vote.')
#     print('Please register to vote as soon as you turn 18!')



# age = 45

# if age < 4:
#     print('Your admission cost is 0.')
# elif age < 18:
#     print('your admission cost is 25.')
# else:
#     print('Your admission cost is 40.')


# age = 70

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f'Your admission cost is {price}.')




# alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print(f'Got 5 you choose {alien_color[0]}')
# if 'yellow' in alien_color:
#     print(f'got 10 you choose {alien_color[1]}')
# if 'red' in alien_color:
#     print(f'got 10 you choose {alien_color[2]}')



# age = 33

# if age < 2:
#     print('newborn')
# elif  age >= 2  and age < 4:
#     print('baby')
# elif age >= 4 and age < 13:
#     print('young')
# elif age >= 13 and  age < 20:
#     print('boy')
# elif age >= 20 and age < 65:
#     print('adult')
# else:
#     print('old!')
#     print(age)



# fruits = ['apple', 'grapes', 'pear']
# a = 'banana'
# if 'banana' in fruits:
#     print('yes')
# if 'banana' not in fruits:
#     print('no')

# fav_fruits = ['apple', 'grapes', 'pear']
# if 'apple' in fav_fruits:
#     print(f'You really like apple!')
# if 'grapes' in fav_fruits:
#     print(f'You really like grapes!')
# if 'pear' in fav_fruits:
#     print(f'You really like pear!')
# if 'banana' in fav_fruits:
#     print(f'You really like banana')
# if 'mush' in fav_fruits:
#     print(f'You really like mush!')




# requested_topping = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_topping:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out green peppers')
#     else:
#         print(f'Adding {requested_topping}.')

#     print('\nFinished making your pizza!')




# requested_topping = []
# if requested_topping:
#     for requested_topping in requested_topping:
#         print(f'Adding {requested_topping}.')
#     print('\nFinished making your pizza!')
# else:
#     print('Are you sure you want a plain pizza?')


# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for i in requested_toppings:
#     if i in available_toppings:
#         print(f'Adding {i}')
#     else:
#         print(f'Sorry, we dont have {i}')



# names = ['admin', 'aiza', 'rauzat', 'kanykei']
# a = ['admin']
# for i in names:
#     if i in a:
#         print(f'Hello {"admin"} would you like to see status report?')
#     else:
#         print(f'Hello {i}, thank you for logging in again')


# names = []
# for i in names:
#     if i in names:
#         print(i)
# else:
#     print('we need to ind some users') 


# current_users = ['admin', 'aiza', 'rauzat', 'kanykei', 'sasha']
# new_users = ['aiza', 'sasha', 'alina', 'albina', 'kira']

# for i in current_users:
#     if i in new_users:
#         print(f'Write new user:{i} ')
#     else:
#         print('error')
        

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in numbers:
#     if i == 1:
#         print('1st')
#     if i == 2:
#         print('2nd')
#     if i == 3:
#         print('3rd')
#     elif i >= 4:
#         print(i,'th')
    



#DICTIONARY


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
    
 
# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print(f'You just earned {new_points} points!')


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position']= 0
# alien_0['y_position']= 25
# print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0) 


# alien_0 = {'color': 'green'}
# print(f'The alien is {alien_0["color"]}.')

# alien_0['color'] = 'yellow'
# print(f'The alien is now {alien_0["color"]}.')


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f'Original position: {alien_0["x_position"]}')

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)



# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil':'python',
#         }
# language = favorite_languages['sarah'].title()
# print(f'Sarahs fav language is {language}.')


# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f'\nKey: {key}')
#     print(f'Value: {value}')


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil':'python',
#         }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s fav language is {language.title()}.")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil':'python',
#         }

# for name in favorite_languages.keys():
#     print(name.title())


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print(f'Total number of aliens: {len(aliens)}')



# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza"
# 'with the following toppings:')

# for topping in pizza['toppings']:
#     print('\t' + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f'\t{language.title()}')


# users = {
#     'einstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton'
#         },

#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         },
# }

# for username, user_info in users.items():
#     print(f'\nUsername: {username}')
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f'\tFull name: {full_name.title()}')
#     print(f'\tLocation: {location.title()}')




# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)


# name = input('please enter your name: ')
# print(f'\nHello, {name}!')

# prompt = 'If you tell us who you are, we can personalize the message you see.'
# prompt += '\nWhat is your first name?'

# name = input(prompt)
# print(f'\nHello, {name}!')



# age = input('How old are you? ')
# age = int(age)
# #age >= 18

# height = input('How tall are you, in inches? ')
# height = int(height)

# if height >= 48:
#     print('\nYou are tall enough to ride!')
# else:
#     print('\nYou will be able to ride when you are a little older.')


# a = 4 % 3
# print(a)

# number = input('Enter a number, and i will tell you if it is evevn or odd: ')
# number = int(number)

# if number % 2 ==0:
#     print(f'\nThe number {number}is even.')
# else:
#     print(f'\nThe number {number} is odd.')

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# prompt = '\nTell me something, and i will repeat it back to you: '
# prompt = "\nEnter 'quit' to end the program."
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(message)






# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f'Verifying user: {current_user.title()}')
#     confirmed_users.append(current_user)
# print('\nThe following users have been confirmed: ')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# pets = ['dog', 'cat', 'dog', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)




#FUNCTIONS

# def greet_user():
#     '''Hello'''
#     print("hello")
# greet_user()

# def greet_user(username):
#     print(f'Hello, {username.title()}!')
# greet_user('jesse')

# def describe_pet(animal_type, pet_name):
#     print(f'\nI have a {animal_type}.')
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')


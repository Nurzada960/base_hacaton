# 1 def...<name>(args):

#     <body>
#     print('logic')
#     <name>(....)

# def send_text():
#     text='мы наконец-то создали данную функцию'
#     print(text)
# send_text()

# def counter():
#     a = int(input('first num: '))
#     b = int(input('second num: '))
#     print('total',a + b )
# counter()




# def hello_name(from_name,old): # обязательные параметры
#     text = f'меня зовут {from_name}, i am {old} years old"'
#     print(text)
# hello_name("Agil","13") # аргументы
# hello_name("Nurzada","18")
# hello_name("Egida","11")
# hello_name("agil","14")


# def country(city):
#     print('я из ' + city)
# country('Chui')
# country('New-York')



# #глобальные и локальные переменные
# def num():
#     f,d,b = 1,2,456546456 # local
#     print(f,b,d)

# f,d,b = 4,6,9 #global

# num()


# def hi():
#     name = 'Agil'
#     print(name)

# name = 'Nurzada'

# print(name)
# hi()


# numbers = [2,3,5,2,6,7,8,3,3,6,4]
# def num():
#     chet = []
#     nechet = []
#     for i in numbers:
#         if i in numbers:
#             if i % 2 ==0:
#                 chet.append(i)
#             print(chet,nechet)
# num()


# def num(numbers = list):
#     chet =[]
# or i in numbers:
#         if i % 2 == 0:
#             chet.append(i)
#         else:
#             nechet.append(i)
#     print('четное', 'chet', 'nechetnoe')
# num([1,34,6,2,5,6,8,9])
# num([2,6,23#     nechet =[]
#     f,23,5,6,33,3])



# def spisok():
#     list_1 = ['name', 'age', '1', '19']
#     x = list_1[1::-1]
#     y = list_1[3:1:-1]
#     print(x+y)
# spisok()

# def fibanacci():
#     f1 = 1
#     f2 = 1
#     a = int(input('Chislo: '))
#     for i in range(a):
#         f1,f2 = f2, f1+f2
#         print(f2,end = '')
# fibanacci()

# def value(x,y):
#     def sum():
#         print(x+y)
#     def subs():
#         print(x-y)
#     sum()
#     subs()
# value(10,10)

# def sum(x,y):
#     print(x+y)

# def subs(x,y):
#     print(x-y)

# def value():
#     subs(20,7)
#     sum(7,6)
# value()

# def meth(a, b):
#     print(a + b, a - b)
# meth(1,2)

# def method_2():
#     method_1()

# def new_file():
#     name= input(': ')
#     a = open(name,mode='w')
#     a.write('ppc')
#     a.close()
# b = new_file
# print(b())



# from random import choice
# def get_number():
#     i = 0
#     print('0444', end='')
#     while i <=5:
#         n2 = [1,4,5,7,9,0]
#         print(choice(n2), end='')
#         i = i + 1
# get_number()















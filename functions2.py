# return
# def hello():
#     return 'Agil where are you my love baby'
# message = hello()
# print(message)


# def sum(a,b):
#     s = a + b 
#     return s 
# print(sum(2,5))


# def squire(x):
#     return x ** 2
# print(squire(3))


# def get_max(a,b):
#     return a if a >b else b
# print(get_max(2,6))




# from math import *
# def cylinder():
#     r = float(input(':        '))
#     h = float(input(':        '))
#     side = 2 * pi * r * h
#     circle = pi * r**2
#     full = side + 2 * circle
#     return full
# print(cylinder())



#args and kwargs     
# *a,b,c = 1,2,3,4
# print(a)
# print(b)
# print(c)


# def name(*args):
#     for i in args:
#         return i
# word =('kak dela s func?')

# print(name(word))



# def find_animal(*args):
#     if 'dog' in args:
#         return True
# print(find_animal('cat', 'mouse', 12,32,False,'dog'))


# def infor(game, **kwargs):
#     players = []
#     numbers = []
#     if game == 'football':
#         for k,w in kwargs.items():
#             players.append(k)
#             numbers.append(w)
#         return game, players, numbers 
# print(infor(game = 'football', alex = 'first', bob = 'second', messi = '10', ronaldo = 'second'))



# def phone_book(**kwargs):
#     name = []
#     phone = []
#     for k,v in kwargs.items():
#         name.append(k)
#         phone.append(v)
#     return name,phone
# print(phone_book(agil = '+996345678', egida = '+9923456'))






# def add(a,b):
#     return a+b
#     def substract():
#         return a-b
#     def multiply():
#         return a*b
#     def divide():
#         return a/b
#     substract()
#     multiply()
#     divide()
# print(add(5,5))


# message = input("строка")
# sum = 0

# def fffff():
#     global message
#     global sum
   
#     for i in message:
#         sum+=1
#     return sum

# print(fffff())


# def dict(a,b):
#     a.update(b)
#     return a 
# a = {input("a: "): input("b: ")}
# b = {input("new: "): input("new2: ")}
# print(dict(a,b))


# def menu():
#     a = input('Would like to drink or eat?')
#     nefail = open('meny.txt',mode ='w')

#     nefail.write(a)
#     nefail.close()
#     return nefail
# print(menu())


# def func_1():
#     print('Я главная функция!')

# def func_2():
#     print('Я вложенная функция!')
# func_2()

# func_1()
# print()




























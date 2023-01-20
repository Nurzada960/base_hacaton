# def recursia(avlue):
#     print(avlue)
#     if avlue < 10:
#         recursia(avlue+1)
#     print(avlue)

# recursia(1)


# lambda - функция(анонимная,можно не присваивать ссылку на обьект, не имеет место в памяти,
# подходит для легких математических задач)
# def f(x):
#     return x **2
# print(f(3))
# aaa = lambda x: x**2
# print(aaa(3))


# aaa = lambda a,b,c: a+b+c
# print(aaa(2,3,4))

# def fun_decorator(func):  #параметр Func ссылка на некую функцию
#     def wrapper():
#         print("яячто то делаю до вызова")
        
#         print("яя что то делаю после вызова ")
#         func()
#     return wrapper


# def some_func():
#     print("вызов функции")

# f =fun_decorator(some_func)
# f()


# list = lambda f,g,h: f*g*h
# list2 = 'Обьем бассейна:   '
# print(list2,list(2,3,4))



# def f(x):
#     return x - 365
# day = 'Прошло:  '
# days = lambda x: x - 365
# day2 = 'Осталось:  '
# print(day,f(346),day2,days(19))

# new_year = lambda x: 365 - x
# print("до нового года осталось ",new_year(19))




# def num(n):
#     print(n)
#     if n == 100:
#         return n
#     else:
#         num(n+2)
# num(1)


def lset(a):
    if a == set():
        return a
    else:
        print(a.pop())
        return lset(a)
print(lset(a={'admin', 'admin2', 'admin3'}))


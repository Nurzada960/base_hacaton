# for i in range(start,stop,step):
#    print(i)

# for i in range(2,10,2):
#    print(i)

# for i in range(1,15):
#     if i == 5:
#         continue
#     print(i)


# for i in range(1,15):
#     if i == 5:
#         break
#     print(i)

# name = 'Nurzada'
# for i in name:
#     print(i, end = '    ')

# name = 'Nurzada'
# for i in name:
#    print(i, end = '')



# n = int(input('input number: '))
# for i in range(1, n+1):
#     print('hello Nurzada')



# n = int(input('input numb: '))
# s = 0
# for i in range(n):
#     message = int(input('new number: '))
#     s += message
#     print(s)
# print('total',s)



# numbers = [1,2,3,4,5,6,7,8,123]
# count = 0
# for i in numbers:
#      print(i)
#     count+=1
# print(count)



# numbers = [2, 3, 6, 9]
# p = 1
# for i in numbers:
#     p*=i
# print(p)


# animals = ('dog', 'panda', 'elephant', 'cat')
# elem = 0
# for elem in range(0,len(animals)):
#     print(animals[elem])
# for i in range(0,len(animals)):
#         print(i)
# for i in animals:
#         print(i)



# count = 0
# text ='ncjdhdbfhdhdbf'
# for i in text:
#     if i == 'd':
#         count+=1
# print('current', count)



#Словарь 

# drinks = {'coca-cola': 45, 'fanta': 47, 'sprite': 34}
# for k,v in drinks.items():
#     print(k,v)
# names=[]
# price=[]
# for name in drinks.keys():
#     names.append(name)
# for value in drinks.values():
#     price.append(value)
# print(names)
# print(price)


#while


# num = 5
# while num < 15:
#     print(num)
# num+=1

# hello = True
# while hello:
#     if input('input something:    ') == 'bye':
#         hello = False




# list1 = ['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']


# for i in list1:
#     print(i)


# list1 = ['ermek', 'azim', 'tima','hattab','baytik','nurzada','aiza','kana','roza','aijan','emir']

# for i in list1:
#     if i == 'ermek':
#         print('Такое имя есть ')
#     elif i == 'azim':
#         list1.remove(i)
#         list1.append('new')        
# print(list1)

# a = 5
# for i in range(1,10):                       
#     print(f'{i} * {a} = {i * a}')

#все умножилось на 5



# a = []
# b = int(input('Enter num: '))
# for i in range(b):
#     a.append(i)
# print(a)


#цикл от 0 итд 


# names = []
# for _ in range(1,10):
#     name = input('Веди имя: ')
#     names.append(name)
# print(names)






#numbers = [1,2,3,4,5,6,7,8,9]

# count = 0
# for i in numbers:
#     count += i
#     print(count)

#накопительный

# count = 0
# for i in numbers:
#     if i == 4:
#         count += 1
#     elif i == 5:
#         print(f'0, это же пять! = {i}')

# print(f'Общеее количество четверок = {count}')

#общее количество четверок
#и 5 тоже

# index1 = int(input('Введи номер индекса: '))
# cities = ['bishkek', 'osh', 'naryn', 'talas', 'kant', 'batken', 'karakol']
# for i in range(len(cities)):
#     if index1 == i:
#          print(cities[i])
#     else:
#         print('Такого индекса нет')

# count = 0
# for i in numbers:
#     if i == 4:
#         count += 1
#     elif i == 5:
#         print(f'0, это же пять! = {i}')



# cities = ['bishkek', 'osh', 'naryn', 'talas', 'kant', 'batken', 'karakol']
# city = input('Введи название города: ')
# for i in cities:
#     if i == city:
#         print('Такой город есть!')







#Задание 1
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

# for lang in languages:
#     if lang == lang1:
#         print("ok")
#     else:
#         print("no")


#задание 2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i) 


#Задание 3


# p = 7
# for num in range(1,6):
#     p*=7
#     print(num)

# print(p)

# a = 7
# i = 0
# while i < 5:
#     a = a*7
#     print(a)
#     i+=1


#задание 4

# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for k,v in enumerate(languages,start=1):
#     print(k,v)

#Задание 5


# for i in range(-9,10):
#     print(10-abs(i),end='')



#задание 6

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)

# for i in range(1):
#     print(names[2:14:2])


#задание 7

# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)

# for i in range(1):
#     print(names[1:14:2])


#Задание 5







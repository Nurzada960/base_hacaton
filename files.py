# file = open("text.txt",mode = "r", encoding= 'utf-8')
# print(file.read())
# file.close()


# file = open("text.txt",mode = "r",encoding="utf-8")

# for line in file:
#     if "Nurzada" in file:
#         print("парниша найден")
#     else:
#         print("no")


# file =open("text.txt",mode = 'r',encoding="utf-8")
# for k,v in enumerate(file,1):
#     print(k,v)

# file.close()

# file2 = open('new.txt',mode = "w" ,encoding="utf-8")
# file2.write("hello world")             #mojno dobavit drugoe nazvanie
# file2.close()


# file3 = open("new2.txt",mode ="a", encoding="utf-8")
# file3.write("hello nurzada")
# file3.close()


# login = input("Введите свой логин: ")
# password = input("Введите свой пароль: ")
# registration = open("name_pas.txt",mode="a",encoding='utf-8')
# registration.write("логин" + "\n")
# registration.write("пароль" + password + "\n")
# registration.close()



# with open("new.txt", mode="a",encoding="utf-8") as f:
#     f.write('как дела')


#Задание 1
# with open("directories.txt", mode="a",encoding="utf-8") as f:
#     f.write('''Applications	Volumes		etc		sbin
# Library		bin		home		tmp
# System		cores		opt		usr
# Users		dev		private		var''')


#Задание 2
# login = input("Введите свой логин: ")
# password = input("Введите свой пароль: ")
# registration = open("users.txt",mode="a",encoding='utf-8')
# registration.write("логин" + "\n")
# registration.write("пароль" + password + "\n")
# registration.close()


#Задание 3

# file2 = open('text.txt',mode = "r" ,encoding="utf-8")

# for letter in file2:
#     if "w" in letter:
#         print("Да в тексте есть W ")
#     else:
#         print('Нет в тексте нет W')

# file2.close()


#Задание 4

# message = '''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.
# '''

# file2 = open('nurzda.txt',mode = "a" ,encoding="utf-8")
# file2.write(message)
# file2.close()
# c = open('python.txt',mode = "w",encoding='utf-8')
# r = c.read().split()
# t_words =[]
# for letter in r:
#     if"t" in letter or "T" in letter:
#         t_words.append(letter)
#     print(t_words)




#Задание 5


# login = input("Введите свой логин: ")
# password = input("Введите свой пароль: ")
# file = open("database.txt",mode = "w" ,encoding='utf-8')
# file.write('логин' + login +"\n")
# file.write("пароль" + password +"\n")
# file.write('логин' + login +"\n")
# file.write("пароль" + password +"\n")


# for line in login:
#     if "nur" in login:
#         print(f'already have, regis again pls')
    
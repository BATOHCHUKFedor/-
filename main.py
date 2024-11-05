# name = input("Введите имя:") #str (string) - строка
# age = int(input("Введите возраст:")) #int (integer) - целое число
# point = float(input("Введите оценку:")) #float - число с плавающей точкой (дробное число)
# is_active = bool(input("Введите активность:")) #bool (True/False) - истина или ложь
#
#
#
# print("Тип данных переменной age:", type(age)) #type() - позволяет узнать к какому типу данных принадлежит переменная
# print("Тип данных переменной point:", type(point))
# print("Тип данных переменной name:", type(name))
# print("Тип данных переменной is_active:", type(is_active))
# print("Имя:",name,"Возраст:", age,"Оценка:", point,"Активность:", is_active)
#
# print(float(4))
# print(str(5))
# print(int(4.5))

# a = int(input("Введите число a:"))
# b = int(input("Введите число b:"))
# Арифметические операторы
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) #обычное деление
# print(a // b) #целочисленное деление
# print(a % b) #нахождение остатка от деления
# print(a ** b) #возведение в степень
#Операции сравнения
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
#Логические операторы
# print((a == b) and (a > b))
# print((a == b) or (a > b))
# print(not(a > b))
# #Операторы присваивания
# a = a + 10
# a += 10
# a -= 10
# a /= 10
# a *=  10
# a **= 10
# print(a)
# a = int(input("Введите число a:"))
#
# if a > 10:
#     print("a > 10")
# elif a == 10 and b == 4:
#     print("a == 10")
# elif a == 13:
#     print("a == 13")
# else:
#     print("Неизвестное число")

#Тернарный оператор
# print("a == 10 и b == 4" if a == 10 and b == 4 else "Неизвестное число")
# print("Чётное" if a % 2 == 0 else "Нечётное")

#Цикл while
# a = int(input("Введите число a:"))
# while a <= 10:
#     print(a)
#     a += 1
#
# print("Мы уже не в цикле!")

# Цикл for
# a = int (input("введите число a:"))
# b = int (input("введите число b:"))
# for i in range(1, 10):
#     if i == 5:
#         continue
#         print(i)

# Оператор выбора match-case
# a = (input("введите значение:"))
# match a:
#     case "+": print(10 + 9)
#     case "-": print(10 - 9)
#     case "*": print(10 * 9)
#     case "/": print(10 / 9)
#     case _: print("Неизвестное число")

# Списки
# names = ["Петя", "Вася", "Коля"]
# print(names)
# print(names[0], names[1], names[2])
# print(names[-1], names[-2], names[-3])
#
# # Добавление
# names.append("Коля") #Добавление нового элемента в конец списка
# print(names)
# names.insert(3, "Эдик") #Добавление нового элемента на определенную позицию (индекс)
# print(names)
# names.extend([1, 2]) #Добавляет все элементы из другого списка в конец текущего списка
# print(names)
# #Удаление
# names.remove(1) #Удаляет первый найденный элемент из списка
# print(names)
# name = names.pop() #Удаляет и возвращает элемент с указанного индекса
# #(По умолчанию последний элемент)
# print("Удалённый элемент:", name)
# print(names)
# del names[0] #Удаление элемента по индексу
# print(names)
# # names.clear()
# # print(names)
# #Поиск элементов
# print(names.index("Вася")) #Возвращает индекс первого найденного элеменнта
# print(names.count("Коля")) #Возвращает количество вхождений элемента в список
# #Сортировка
# numbers = [2, 3, 5, 2, 1, 3, 22]
# numbers.sort(reverse=True)
# print("Числа:", numbers)
# names.sort(reverse=True) #Сортировка в алфавитном порядке либо (если число) от меньшего к большему
# print(names)
# names.reverse() #Сортировка в обратном порядке
# print(names)
# print(len(names)) #Возвращает количество элементов в списке
# print(len(numbers))
#Срезы
#[start:end:step]
# print(names[1:-1])
# print(numbers[1:])
# print(numbers[:3])
# print(numbers[::2])
# print(numbers[1::2])

#Вложенные списки
# numbers = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# print(numbers[1][2])
#
# for i in numbers:
#     for j in i:
#         print(j)

#Генератор списков
# numbers = [i for i in range(1, 21, 2)]
# print(numbers)
# print(min(numbers), max(numbers), sum(numbers))

#Конкатенация
# print([1, 2, 3] + [4, 5, 6])
# print("строка" + "авааа")
# print([1, 2, 3] * 3)

#
# numbers = [1, 2, 3, 6, 7]
# a, b, c, d = numbers
# print(a, b, c, d)

# a, *b, c, d = numbers
# print(a, b, c, d)

# a, _, b, _, _, = numbers
# print(a, b)

#Кортеж (tuples)
# names = ("Петя", "Вася", "Коля", "Вася")
# print(names[0], names[1], names[2])
# print(names[-1], names[-2], names[-3])
# #names[0] = "Эдик"
# print(names[1:])
# print((1, 2, 3) + (4, 5))
# print((1, 2, 3) * 3)
# # a, b, c = names
# # print(a, b, c)
#
# print(names.count("Вася"))
# print(names.index("Вася"))
#
# numbers = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
# )
# print(numbers[1][1])
#
# for i in numbers:
#     for j in i:
#         print(j)

#Множества (Sets)
# names = {"Петя", "Вася", "Коля", "Вася"} #Для хранения данных с уникальными значениями
# names1 = {"Катя", "Вера", "Соня", "Коля"}
# #Объединение
# print(names.union(names1))
# print(names | names1)
# #Пересечение
# print(names.intersection(names1))
# print(names & names1)
# #Разность
# print(names1.difference(names))
# print(names1 - names)
# #Симметричная разность
# print(names.symmetric_difference(names1))
# print(names ^ names1)

# print(names)
# names.add("Эдик") #Добавляет элемент в множество
# print(names)
# # names.remove("Сеня") #Удаляет указанный элемент. Если элемента нет в множестве, возникает ошибка KeyError
# # print(names)
# names.discard("Сеня") #Удаляет указанный элемент, но не вызывает ошибку, если элемента нет
# print(names)
# name = names.pop() #Удаляет и возвращает случайный элемент в множество
# print(name, names)
# names.clear()
# print(names)

# Словари
# student = {
#     "name": "Петя",
#     "age": 18,
#     "marks": [85, 92, 78, 90]
# }
# print(student)
# print(student["name"], student["age"], student["marks"])
#
# student["age"] = 20 #Изменение значения
# print(student)
# student["city"] = "Москва" #Добавление новой пары "ключ: значение"
# print(student)
# del student["city"] #Удаление с помощью оператора del
# print(student)
# name = student.pop("name") #Удаление и возвращает удалённое значение по ключу
# print(name, student)
# student.clear() #Очистка словаря
# print(student)
#
# Методы словарей
# print(student["name"])
# print(student.get("name", "Неизвестное значение")) #Возвращает значение для указанного ключа,
# если ключ существует. Если ключ не существует, вовращает значение по умолчанию (по умолчанию - None)
# print(list(student.keys())) #Получение всех ключей
# print(list(student.values())) #Получение всех значений
# print(list(student.items())) #Получение всех пар ключ-значение
# student.update({"group": "П-2-23", "id_student": "1"}) #Обновляет словарь, добавляя пары ключ-значение из другого словаря
# print(student)
# for i in student:
#     print(i, student[i])
#
# for key, value in student.items():
#     print(key, value)
#
# group = [
#     {"name": "Петя", "marks": [85, 92, 78, 90], "city": "Москва"},
#     {"name": "Вася", "marks": [85, 92, 78, 90], "city": "Санкт-Петербург"},
#     {"name": "Коля", "marks": [85, 92, 78, 90], "city": "Новосибирск"}
# ]
# print(group)
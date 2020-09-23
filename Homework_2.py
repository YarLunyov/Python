# Задача 1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 'Hi', 7.89, ['h', 'e', 'l', 'l', 'o'], True]
for i in my_list:
    print(type(i))

# Задача №2
# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().
start_list = list(input('Введите любую последовательность: '))  # например 1z2x3c4
for el in range(1, len(start_list), 2):
    start_list[el - 1], start_list[el] = start_list[el], start_list[el - 1]
print(start_list)

# Задача №3
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

my_month = int(input('Введите номер месяца года: '))  # решение через словарь
month_dict = {1: 'Зима', 2: 'Зима',
              3: 'Весна', 4: 'Весна', 5: 'Весна',
              6: 'Лето', 7: 'Лето', 8: 'Лето',
              9: 'Осень', 10: 'Осень', 11: 'Осень',
              12: 'Зима'}
print(month_dict[my_month])

my_month = int(input('Введите номер месяца года: '))  # решение через список
month_list = ['_', 'Зима', 'Зима',
              'Весна', 'Весна', 'Весна',
              'Лето', 'Лето', 'Лето',
              'Осень', 'Осень', 'Осень',
              'Зима']
print(month_list[my_month])

# Задача №4
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, выводить
# только первые 10 букв в слове.

my_str = input('Введите любую строку: ')
my_list = my_str.split()
for el in range(0, len(my_list)):
    print(el + 1, my_list[el][:10])

# Задача №5
# Реализовать структуру « Рейтинг » , представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
# Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
my_num = int(input('Введите вашу оценку от 1 до 10: '))
for el, number in enumerate(my_list):
    if my_num <= my_list[el]:
        continue
    my_list.insert(el, my_num)
    print(my_list)
    break
else:
    my_list.insert(el+1, my_num)
print(my_list)

# Задача №6
# *Реализовать структуру данных « Товары » . Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

i_tuple = []
num = 1
analitycs_dict = {'Название': [],
                  'Цена': [],
                  'Количество': [],
                  'Единица измерения': []}
while True:
    if input('Выход - E, \nЛюбая клавиша - продолжить: ') == 'E':
        break
    temp_dict = {'Название': input('Введите название: '),
                 'Цена': input('Введите цену: '),
                 'Количество': input('Введите количество: '),
                 'Единица измерения': input('Введите единицу изм. :')}
    # analitycs_dict = {'Название': [],
    #                   'Цена': [],
    #                   'Количество': [],
    #                   'Единица измерения': []}
    i_tuple.append((num, temp_dict))
    print(i_tuple)
    num += 1
# Не понимаю, как в аналитику добавить новые values к существующим...  .append(temp_dict['Название'])...
    # i_val = []
    # j_val = []
    # k_val = []
    # l_val = []
    # analitycs_dict = {'Название': [],
    #                   'Цена': [],
    #                   'Количество': [],
    #                   'Единица измерения': []}
    for i in temp_dict.keys():
        analitycs_dict[i].append(temp_dict[i])
        # i_val.append(temp_dict['Название'])
        # j_val.append(temp_dict['Цена'])
        # k_val.append(temp_dict['Количество'])
        # l_val.append(temp_dict['Единица измерения'])
    for key, value in analitycs_dict.items():
        print(key, value)

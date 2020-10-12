#  Задача №1
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

"""Строки
Наступила осень
Пожелтел наш сад
Листья на берёзе
Золотом горят"""

f_1 = open("HW5_my_file_1", 'w')
while True:
    my_line = input('Введите информацию: ')
    if my_line == '':
        break
    f_1.write(my_line + '\n')
f_1.close()

# Задача №2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open("HW5_my_file_1.txt") as f:
    content = f.readlines()
    print(content)
    print('Количество строк в файле =', len(content))
    for i, number in enumerate(content):
        my_str = content[i].split()
        print(f'Количество слов в строке №{i + 1} =', len(my_str))

# Задача №3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("HW5_my_file_2.txt") as f_3:
    content_3 = f_3.readlines()
#    print(content_3)
    print('Сотрудники с окладом менее 20 тыс: ')
    sum_salary = 0
    for i in content_3:
        surname, salary = i.split()
        sum_salary += float(salary)
        if float(salary) < 20000:
            print(surname)
    print('ФЗП: ', sum_salary)
    average = sum_salary / len(content_3)
    print('Средний оклад сотрудника: ', round(average, 2))

# Задача №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

with open("HW5_my_file_4_eng.txt") as f_4:
    for line in f_4:
        word, num = line.split(' - ')
        if word == 'One':
            word = 'Один'
        elif word == 'Two':
            word = 'Два'
        elif word == 'Three':
            word = 'Три'
        else:
            word = 'Четыре'
        f_4_res = open("HW5_my_file_4_rus.txt", 'a')
        f_4_res.write(word + ' - ' + num)
        f_4_res.close()

# Задача №5
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

with open("HW5_my_file_5.txt", 'w', encoding='utf-8') as f_5:
    temp_line = input('Введите числа разделённые пробелами: ')
    f_5.write('Введены следующие числа: ' + temp_line + '\n')
    my_list = temp_line.split()
    my_list = ([int(i) for i in my_list])
    my_sum = 0
    for i in my_list:
        my_sum += int(i)
    f_5.write('Сумма введённых чисел: ' + str(my_sum) + '\n')
    print('Введены следующие числа: ', temp_line)
    print('Сумма введённых чисел: ', my_sum)
    print('Запись в файл выполнена')



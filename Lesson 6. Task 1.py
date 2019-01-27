# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import sys
from collections import deque

# import gc
# import heapq
# import pickle
# import shelve

# В идеале - Функция создавалась, для возврата списка из ссылок на объекты, создаваемых в ходе исполнения скрипта файла, путь к  которому передается на вход.
# В итоге: не получилось реализовать в виде списка ссылок на создаваемые объекты, получилось только реализовать список из строковых значений, равных наименованию объектов.
# На вход получает путь к файлу, на выходе возвращает наименования объектов в виде строковых объектов.
def find_object_in_file(path_file):
    import os
    l_file = []
    file_ob = open(path_file, 'r', encoding='UTF-8')
    text_obj = open('text_less.txt', 'w', encoding='UTF-8')
    wanted_symbol = ' = '
    str_obj_list = file_ob.readlines()
    for line in str_obj_list:
        if wanted_symbol in line:
            end_str = line.find(wanted_symbol)
            if end_str > 0:
                nn = line[:end_str]
                beg_str = nn.rfind(' ')
                mm = line[beg_str+1:end_str]
                l_file.append(mm)
                text_obj.writelines(mm +'\n')
    file_ob.close()
    text_obj.close()
    return l_file


def show_size(x, level=0):
    print(f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


def get_obj (*args):
    import gc
    return gc.get_referents(args)


def show_mem_size(*args):
    list_object = [args]
    for i in list_object:
        if hasattr(i, 'items'):
            show_size(get_obj(i))
        else:
            show_size(i)


def s_10_to_16(a):
    mass_a = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F', }
    return mass_a[a]


def s_16_to_10(b):
    mass_b = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15, }
    return mass_b[b]


def num_16_to_10(c):
    numm = 0
    for i in range(len(c)):
        numm += s_16_to_10(c[i]) * (16 ** i)
    return numm


def num_10_to_16(c):
    n = 1
    while (c // 16 ** n) > 16:
        n += 1
    numm = []
    numm.append(s_10_to_16(c // 16 ** n))
    ab = c - s_16_to_10(numm[0]) * (16 ** n)
    for i in range(1, n + 1):
        numm.append(s_10_to_16(ab // (16 ** (n - i))))
        ab = ab - s_16_to_10(numm[i]) * (16 ** (n - i))
    return numm



n_1 = str.upper(input('Введите первое число в 16-й системе = '))
n_2 = str.upper(input('Введите первое число в 16-й системе = '))

if n_1[0] == '-':
    x = deque(n_1[1:])
    x_sign = -1
else:
    x = deque(n_1)
    x_sign = 1

if n_2[0] == '-':
    y = deque(n_2[1:])
    y_sign = -1
else:
    y = deque(n_2)
    y_sign = 1

x.reverse()
y.reverse()
x_x = x_sign * num_16_to_10(x)
y_y = x_sign * num_16_to_10(y)
plus_xy = x_x + y_y
mult_xy = x_x * y_y
deq_plus_xy = []
deq_mult_xy =[]

if plus_xy < 0:
    plus_xy_sign = -1
    plus_xy_abs = abs(plus_xy)
    deq_plus_xy.append('-')
    deq_plus_xy.append(num_10_to_16(plus_xy_abs))
else:
    plus_xy_sign = 1
    plus_xy_abs = abs(plus_xy)
    deq_plus_xy.append(num_10_to_16(plus_xy_abs))

if mult_xy <0:
    mult_xy_sign = -1
    mult_xy_abs = abs(mult_xy)
    deq_mult_xy.append('-')
    deq_mult_xy.append(num_10_to_16(mult_xy_abs))
else:
    mult_xy_sign = 1
    mult_xy_abs = abs(mult_xy)
    deq_mult_xy = num_10_to_16(mult_xy_abs)


print(f' Сумма чисел {n_1, n_2} равна = {deq_plus_xy}')
print(f' Произведение чисел {n_1, n_2} равно = {deq_mult_xy}')


# 64-разрядная ОС, скорее всего интерпретатор 32-битный
# Расчет занимаемой памяти через выявления объектов создаваемых в скрипте "вручную"
list_object = [x, y, n_1, n_2, deq_plus_xy, deq_mult_xy ]
# Выявления размера памяти через задание объектов вручную в list
show_mem_size(list_object)


ww = find_object_in_file('C:/Искусственный интеллект/Pull-requests. Homework/Homework. Python algorithms and structures/Lesson 6. Task 1.py')
print(ww) # нахождене переменных, создаваемых в скрипте файла

# Неудачное реализация ссылок на объекты, создаваемых в файле, через список, возвращаемую функцией find_object_in_file
# [l_file, file_ob, text_obj, wanted_symbol, str_obj_list, end_str, nn, beg_str, mm, mass_a, mass_b, numm, n, ab, n_1, n_2, x, x_sign, y, y_sign, x_x, y_y, plus_xy, mult_xy, deq_plus_xy, plus_xy_sign, plus_xy_abs, mult_xy_sign, mult_xy_abs, w, ww, rr]
# for i in ww:
#     show_size(i)

# Реализация вывода объектов через файл, но сохранить объекты с сохранением ссылок и типа объекта не удалось.
#  Но можно вручную перебрать данные объекты из файла и передать функции  show_size, как например в циshow_size(dew
# rr = open('text_less.txt', 'r', encoding='UTF-8')
# print(rr)
# for i in rr:
#     show_size(i)

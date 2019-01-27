# Используя конспект, написать программу сложения и умножения
# двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого – это цифры числа.

from collections import deque
import sys

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


def get_obj(*args):
    import gc
    return gc.get_referents(args)


def show_mem_size(*args):
    list_object = [args]
    for i in list_object:
        if hasattr(i, 'items'):
            show_size(get_obj(i))
        else:
            show_size(i)


BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(hex_num):
    deq_hex_num = deque(hex_num.upper())
    return deq_hex_num


def sum_hex(first, second):
    """
    Изменяемые объекты передаются по ссылке
    Используем копию, чтобы не ломать оригинал
    """
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    for i in range(len(first) - 1, -1, -1):
        first_num = BIN_NUMBERS[first[i]]
        second_num = BIN_NUMBERS[second[i]]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    for i in range(len(first) - 1, -1, -1):
        second_num = BIN_NUMBERS[second[i]]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - i - 1))
        result = sum_hex(result, spam)

    return result


if __name__ == '__main__':
    a = input('Введите первое число в hex формате (только цифры от 0 до f): ')
    b = input('Введите второе число в hex формате (только цифры от 0 до f): ')

    a = convert(a)
    b = convert(b)

    print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
    print(f'{a} * {b} = {mult_hex(a, b)}')  # специально убрал список, чтобы показать как хранится


# 64-разрядная ОС, скорее всего интерпретатор 32-битный
# Расчет занимаемой памяти через выявления объектов создаваемых в скрипте "вручную"
# Взят за основу скрипт преподавателя
list_object = [a, b, list(sum_hex(a,b)), list(mult_hex(a,b))]
# Выявления размера памяти через задание объектов вручную в list
show_mem_size(list_object)

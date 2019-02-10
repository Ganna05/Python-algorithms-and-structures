# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
# 1) посчитать частоту символов
# 2) построить дерево, основываясь на сумме частот первых двух элементов с наименьшей частотой
# 3) построить таблицу кодировок на методе "щаг вправо=1, шаг влево=0", т.е. шагая по дереву
# 4) выдать кодировку строки, основываясь на кодах в таблице кодировок

import collections
import copy
import operator


def by_value(node):
    return node.value


def create_tree(args):
    b = sorted(args, key=by_value)
    if len(b) > 1:
        node = MyNode('', (b[0].value + b[1].value), b[0], b[1])
        b = b[2:]
        b.append(node)
        return create_tree(b)
    else:
        return b


def search(node_char, args, path=''):
    ls = node_char
    v = args
    if v[0].value == ls.value and v[0].name == ls.name:
        return f'{path}'
    if v[0] is not None and ls.value != v[0].value and ((v[0].left is not None and v[0].left.value == ls.value)
                                                        or (v[0].right is not None and v[0].right.value == ls.value)):
        if v[0].left.name == ls.name:
            return f'{path}0'
        if v[0].right.name == ls.name:
            return f'{path}1'
        if v[0].left.name != ls.name and v[0].right.name == '':
            return search(ls, [v[0].right], path=f'{path}1')
        if v[0].right.name != ls.name and v[0].left.name == '':
            return search(ls, [v[0].left], path=f'{path}0')
    if v[0] is not None and v[0].left is not None and v[0].right is not None:
        if ls.value != v[0].value and ls.value != v[0].left.value and v[0].left.name == '' and v[0].right.name != '':
            return search(ls, [v[0].left], path=f'{path}0')
        if ls.value != v[0].value and ls.value != v[0].right.value and v[0].right.name == '' and v[0].left.name != '':
            return search(ls, [v[0].right], path=f'{path}1')
        if ls.value != v[0].value and ls.value != v[0].left.value and ls.value != v[0].right.value:
            a1 = search(ls, [v[0].left], path=f'{path}0') if v[0].left.left is not None else ''
            a2 = search(ls, [v[0].right], path=f'{path}1') if v[0].left.right is not None else ''
            a1 = '' if operator.is_(a1, 'Не найдено') else a1
            a2 = '' if operator.is_(a2, 'Не найдено') else a2
            path = a1 + a2
            return f'{path}'
    return f'Не найдено'


d = input("Введите текст который надо зашрифровать с помощью алгоритма Хаффмана: ")
c = collections.Counter(d)
count_d = c.most_common()
count_d.reverse()
# print(count_d, type(count_d))
MyNode = collections.namedtuple('Node', ['name', 'value', 'left', 'right'])  # для создания узлов дерева
ls_string = []

for i in range(len(count_d)):
    node = MyNode(count_d[i][0], count_d[i][1], None, None)
    ls_string.append(node)

# print(ls_string)  #Структура листьев в виде узлов
tree = create_tree(ls_string)
# print(tree)   #Структура дерева из узлов

t_code_d = {}
for i in range(len(ls_string)):
    t_code_d[ls_string[i].name]= search(ls_string[i], tree)

code_d = str()
for i in range(len(d)): #"Кодирование строки"
    code_d += t_code_d[d[i]] + ' '

print(f'На шифрование отдан следующий текс:"\n{d}')
print(f'Таблица кодировки, "сивол":"код"\n{t_code_d}')
print(f'Шифр данного текста, зашрифрован с помощью алгоритка Хаффмана:" \n{code_d}')
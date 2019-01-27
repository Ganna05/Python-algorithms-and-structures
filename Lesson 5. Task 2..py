# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


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
# print(x)
# print(y)

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

# print(x_sign * num_16_to_10(x), y_sign * num_16_to_10(y))
print(f' Сумма чисел {n_1, n_2} равна = {deq_plus_xy}')
print(f' Произведение чисел {n_1, n_2} равно = {deq_mult_xy}')

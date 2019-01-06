# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
min_item = -30
max_item = 100

array_1 = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(f'Дан одномерный массив чисел {array_1}')
print('Необходимо найти сумму элементов, находящихся между минимальным и максимальным числом')
min_index, min_sp = 0, array_1[0]
max_index, max_sp = 0, array_1[0]

for i in range(1, len(array_1)):
    if array_1[i] < min_sp:
        min_index = i
        min_sp = array_1[i]
    if array_1[i] > max_sp:
        max_index = i
        max_sp = array_1[i]

print(f'Минимальное число {min_sp} - его индекс {min_index}')
print(f'Максимальное число {max_sp} - его индекс {max_index}')

summa = 0
n = max_index - min_index
if n > 0:
    for i in range(n - 1):
        summa += array_1[min_index + i + 1]
else:
    for i in range(abs(n) - 1):
        summa += array_1[max_index + i + 1]

print(f'Сумма чисел между минимальный и максимальным числами - {summa}')

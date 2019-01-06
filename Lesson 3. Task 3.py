# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
min_item = 3
max_item = 100

array_1 = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(f'Дан массив целых чисел {array_1}, необходимо поменять местами минимальное число и максимальное число')
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

array_1[min_index], array_1[max_index] = array_1[max_index], array_1[min_index]
print(f'Минимальное число и максимальное число поменялись местами - {array_1}')
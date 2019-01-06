# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
min_item = 3
max_item = 50

array_num = [random.randint(min_item, max_item) for _ in range(SIZE)]  # Массив-оригинал
print(f'Дан массив чисел {array_num}.')
print('Необходимо определить какое число в массиве встречается чаще всего')

ar_set = list(set(array_num))
array_count = []
max_count = 0

# как можно реализовать- чтобы число элементов array_num уменьшать за счет удаления из массива подсчитанного элемента. При pop() цикл  for перепрыгивает.????
for i in range(len(ar_set)):
    count = 0
    for j in range(len(array_num)):
        if ar_set[i] == array_num[j]:
            count += 1
    if max_count < count:
        max_count = count
    array_count.append(count)

# print(f'Уникальные (неповторяющиеся) числа данного массива  {ar_set}')
# print(f'Встречаются в массиве по столько раз соответственно {array_count} ')

# Массив, из наиболее часто встречающихся чисел массива-оригинала
array_max = [ar_set[i] for i in range(len(ar_set)) if array_count[i] == max_count]

print(f'Чаще всего встречаются следующие числа:{array_max}, по {max_count} раза')

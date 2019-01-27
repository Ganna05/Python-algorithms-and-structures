# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 30
min_item = -20
max_item = 50

array_num = [random.randint(min_item, max_item) for _ in range(SIZE)]  # Массив-оригинал
print(f'Дан массив чисел {array_num}')
print('Необходимо в массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве')

ar_minus = [[array_num[i], i] for i in range(len(array_num)) if array_num[i] < 0]
#print(f'Отрицательные числа в массиве - и их позиции {ar_minus}')

if len(ar_minus) > 0:
    cur_minus = ar_minus[0][0]
    i_cur_minus = ar_minus[0][1]
    for i in range(1, len(ar_minus)):
        if ar_minus[i][0] > cur_minus:
            cur_minus = ar_minus[i][0]
            i_cur_minus = ar_minus[i][1]
    i_array = [ar_minus[i][1] for i in range(len(ar_minus)) if ar_minus[i][0] == cur_minus]
    print(f'В массиве чисел максимальный отрицательный элемент = {cur_minus} и он представлен на позиции {i_array}')
else:
    print('В массиве нет отрицательных цифр.')



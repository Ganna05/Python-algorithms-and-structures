# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
min_item = -30
max_item = 100

array_1 = [random.randint(min_item, max_item) for _ in range(SIZE)]
print(f'Дан одномерный массив чисел {array_1}')
print('Необходимо найти два наименьших элемента')

if len(array_1) > 2:
    min_ind_1, min_sp_1 = 0, array_1[0]
    min_ind_2, min_sp_2 = 1, array_1[1]
    for i in range(2, len(array_1)):
        if min_sp_1 > min_sp_2:
            if array_1[i] < min_sp_1:
                min_ind_1 = i
                min_sp_1 = array_1[i]
        elif min_sp_2 > min_sp_1:
            if array_1[i] < min_sp_2:
                min_ind_2 = i
                min_sp_2 = array_1[i]
        elif min_sp_1 == min_sp_2:
            if array_1[i] < min_sp_1:
                min_ind_1 = i
                min_sp_1 = array_1[i]
    if min_sp_1 < min_sp_2:
        print(f'Два наименьших числа {min_sp_1, min_sp_2} - их индексы {min_ind_1, min_ind_2}')
    else:
        print(f'Два наименьших числа {min_sp_2, min_sp_1} - их индексы {min_ind_2, min_ind_1}')

elif len(array_1) == 2:
    print(f'Массив представлен из двух чисел - они и представлены {array_1}')
else:
    print(f'Массив не удовлетворяет условию, чтобы найти два наименьших числа, т.к. представлен в виде элементов в количестве менее 2.')

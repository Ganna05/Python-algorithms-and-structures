# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

column = 10
line = 10
min_item = -20
max_item = 50

array_num = [[random.randint(min_item, max_item) for _ in range(column)] for _ in range(line)]  # Массив-оригинал
print(f'Дан массив чисел')
for j in range(column):
    print(array_num[j])
print('Необходимо в массиве найти максимальный элемент среди минимальных элементов столбцов матрицы.')

ar_min_in_column = []
for j in range(column):
    min_in_column = array_num[0][j]
    for i in range(1, line):
        if array_num[i][j] < min_in_column:
            min_in_column = array_num[i][j]
            i_min = i
        j_min = j
    ar_min_in_column.append([min_in_column, i_min, j_min])

max_min_in_column = ar_min_in_column[0][0]
for i in range(1, column):
    if ar_min_in_column[i][0] > max_min_in_column:
        max_min_in_column = ar_min_in_column[i][0]

print(f'Минимальные числа по столбцам, Число - Строка - Столбец')
print(f'{ar_min_in_column}')
print(f'Максимальное среди минимальных в столбцах {max_min_in_column}')

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

import random

min_num = 2
max_num = 10
s_num = abs(max_num - min_num)
sp_number = [(min_num + i) for i in range(s_num)]
sp_count = [0 for _ in range(s_num)]

# sp_number = (2, 3, 4, 5, 6, 7, 8, 9,)
# sp_count = [0, 0, 0, 0, 0, 0, 0, 0, ]

SIZE = 10
min_item = 2
max_item = 100

array_1 = [random.randint(min_item, max_item) for _ in range(SIZE)]

for a in array_1:
    j = 0
    for j in range(len(sp_number)):
        if sp_number[j] != 0 and a % sp_number[j] == 0:
            sp_count[j] += 1

# Вывод на экран результата
print(f'В списке чисел {array_1}')
for i in range(len(sp_number)):
    print(f'Числу {sp_number[i]} - кратно {sp_count[i]} числа из списка.')

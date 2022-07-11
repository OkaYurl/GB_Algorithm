"""
Задача 3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

size = 10
my_array = [random.randint(-10, 10) for _ in range(size)]
print(my_array)

index_min = 0
index_max = 0
for i in range(1, len(my_array)):
    if my_array[i] > my_array[index_max]:
        index_max = i
    if my_array[i] < my_array[index_min]:
        index_min = i
my_array[index_min], my_array[index_max] = my_array[index_max], my_array[index_min]

print(my_array)

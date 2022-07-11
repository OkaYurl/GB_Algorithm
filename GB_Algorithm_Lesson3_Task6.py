"""
Задача 6.
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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

if index_min > index_max:
    index_min, index_max = index_max, index_min
sum_between = 0
for i in range(index_min+1, index_max):
    sum_between += my_array[i]
print(sum_between)

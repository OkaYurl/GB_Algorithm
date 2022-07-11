"""
Задача 7.
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random

size = 10
my_array = [random.randint(-10, 10) for _ in range(size)]
print(my_array)

# предположим, что массив можно сортировать
for i in range(0, len(my_array)):
    for j in range(i + 1, len(my_array)):
        if my_array[i] > my_array[j]:
            my_array[i], my_array[j] = my_array[j], my_array[i]

print(my_array)
print(my_array[0], my_array[1])


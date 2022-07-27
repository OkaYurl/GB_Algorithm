"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from deep_getsize import deep_getsizeof


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
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
    print('Целое число, определяющее размерность массива\списка занимает байт: ', deep_getsizeof(size, set()))
    print('Массив\список занимает байт: ', deep_getsizeof(my_array, set()))
    print('index_min занимает байт: ', deep_getsizeof(index_min, set()))
    print('index_max занимает байт: ', deep_getsizeof(index_max, set()))
    print('i занимает байт: ', deep_getsizeof(i, set()))
    return


min_max(10)

# Целое число, определяющее размерность массива\списка занимает байт:  28
# Массив\список занимает байт:  464
# index_min занимает байт:  28
# index_max занимает байт:  28
# i занимает байт:  28

"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from deep_getsize import deep_getsizeof


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
    maxi = my_array.index(max(my_array))
    mini = my_array.index(min(my_array))
    my_array[maxi], my_array[mini] = my_array[mini], my_array[maxi]
    print(my_array)
    print('Целое число, определяющее размерность массива\списка занимает байт: ', deep_getsizeof(size, set()))
    print('Массив\список занимает байт: ', deep_getsizeof(my_array, set()))
    print('maxi занимает байт: ', deep_getsizeof(maxi, set()))
    print('mini занимает байт: ', deep_getsizeof(mini, set()))
    return

min_max(10)

# Целое число, определяющее размерность массива\списка занимает байт:  28
# Массив\список занимает байт:  464
# maxi занимает байт:  28
# mini занимает байт:  28

# Только первый вариант кода занимает на 28 байт памяти больше за счет использования большего количества переменных.
# (Python  3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] win32)

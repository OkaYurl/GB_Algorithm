"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
from deep_getsize import deep_getsizeof


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
    i, j = [f(range(len(my_array)), key=my_array.__getitem__) for f in [min, max]]
    my_array[i], my_array[j] = my_array[j], my_array[i]
    print(my_array)
    print('Целое число, определяющее размерность массива\списка занимает байт: ', deep_getsizeof(size, set()))
    print('Массив\список занимает байт: ', deep_getsizeof(my_array, set()))
    print('i занимает байт: ', deep_getsizeof(i, set()))
    print('j занимает байт: ', deep_getsizeof(j, set()))
    return


min_max(10)

# Целое число, определяющее размерность массива\списка занимает байт:  28
# Массив\список занимает байт:  464
# i занимает байт:  28
# j занимает байт:  28

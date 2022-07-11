"""
Задача 5.
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

size = 10
my_array = [random.randint(-10, 10) for _ in range(size)]
print(my_array)

i = 0
index_max = -1
while i < size:
    if my_array[i] < 0 and index_max == -1:
        index_max = i
    elif my_array[i] < 0 and my_array[i] > my_array[index_max]:
        index_max = i
    i += 1
if index_max != -1:
    print(f'номер позиции: {index_max}, значение: {my_array[index_max]}')
else:
    print('в массиве нет отрицательных элементов')

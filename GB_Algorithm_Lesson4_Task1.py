"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import cProfile


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
    index_min = 0
    index_max = 0
    for i in range(1, len(my_array)):
        if my_array[i] > my_array[index_max]:
            index_max = i
        if my_array[i] < my_array[index_min]:
            index_min = i
    my_array[index_min], my_array[index_max] = my_array[index_max], my_array[index_min]
    return


#  "GB_Algorithm_Lesson4_Task1.min_max(10)" 1000 loops, best of 5: 7.11 usec per loop
#  "GB_Algorithm_Lesson4_Task1.min_max(100)" 1000 loops, best of 5: 69.4 usec per loop
#  "GB_Algorithm_Lesson4_Task1.min_max(1000)" 1000 loops, best of 5: 654 usec per loop

cProfile.run('min_max(1000)')

#  GB_Algorithm_Lesson4_Task1.py 57 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1.py 510 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1.py 5025 function calls in 0.002 seconds

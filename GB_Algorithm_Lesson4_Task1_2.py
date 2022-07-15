"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import cProfile


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
    i, j = [f(range(len(my_array)), key=my_array.__getitem__) for f in [min, max]]
    my_array[i], my_array[j] = my_array[j], my_array[i]
    return


#  min_max(10)

#  "GB_Algorithm_Lesson4_Task1_2.min_max(10)" 1000 loops, best of 5: 8.06 usec per loop
#  "GB_Algorithm_Lesson4_Task1_2.min_max(100)" 1000 loops, best of 5: 71.1 usec per loop
#  "GB_Algorithm_Lesson4_Task1_2.min_max(1000)" 1000 loops, best of 5: 648 usec per loop

cProfile.run('min_max(1000)')

#  GB_Algorithm_Lesson4_Task1_2.py 62 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1_2.py 512 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1_2.py 5034 function calls in 0.002 seconds

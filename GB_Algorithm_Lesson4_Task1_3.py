"""
Задача 3.
В массиве целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import cProfile


def min_max(n):
    size = n
    my_array = [random.randint(-1000, 1000) for _ in range(size)]
    maxi = my_array.index(max(my_array))
    mini = my_array.index(min(my_array))
    my_array[maxi], my_array[mini] = my_array[mini], my_array[maxi]
    return


#  min_max(10)

#  ""GB_Algorithm_Lesson4_Task1_3.min_max(10)" 1000 loops, best of 5: 7.11 usec per loop
#  "GB_Algorithm_Lesson4_Task1_3.min_max(100)" 1000 loops, best of 5: 62.5 usec per loop
#  "GB_Algorithm_Lesson4_Task1_3.min_max(1000)" 1000 loops, best of 5: 616 usec per loop

cProfile.run('min_max(1000)')

#  GB_Algorithm_Lesson4_Task1_3.py 59 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1_3.py 512 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task1_3.py 5032 function calls in 0.002 seconds

#  данный код относительно лучший, т.к. использование циклов сведено к минимуму, эффективно работают встроенные функции.


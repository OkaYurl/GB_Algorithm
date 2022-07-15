"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Второй — без использования «Решета Эратосфена».
"""

import cProfile

def primes_simple(m):
    my_array = [i for i in range(m ** 2)]
    if m == 1:
        return 2
    elif m <= 0:
        return 'i<=0'
    else:
        my_array[1] = 0
        primes = []
        for i in range(2, len(my_array)):
            for num in primes:
                if my_array[i] % num == 0:
                    break
            else:
                primes.append(my_array[i])
            if len(primes) == m:
                return primes[-1]


#  "GB_Algorithm_Lesson4_Task2_2.primes_simple(3)" 1000 loops, best of 5: 971 nsec per loop
#  "GB_Algorithm_Lesson4_Task2_2.primes_simple(10)" 1000 loops, best of 5: 5 usec per loop
#  "GB_Algorithm_Lesson4_Task2_2.primes_simple(100)" 1000 loops, best of 5: 375 usec per loop

cProfile.run('primes_simple(100)')

#  GB_Algorithm_Lesson4_Task2_2.py 13 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task2_2.py 44 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task2_2.py 646 function calls in 0.001 seconds

#  классический алгоритм поиска простых чисел быстрее и эффективнее Эратосфена, к тому же
# есть возможность оптимизации (например, с квадратными корнями)

"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
"""

import cProfile

def primes_era(m):
    my_array = [i for i in range(m ** 2)]
    if m == 1:
        return 2
    elif m <= 0:
        return 'i<=0'
    else:
        my_array[1] = 0
        i = 2
        primes = []
        while len(primes) < m:
            if my_array[i] != 0:
                primes.append(my_array[i])
                j = i * 2
                while j < len(my_array):
                    my_array[j] = 0
                    j += i
            i += 1
        return primes[-1]


#  "GB_Algorithm_Lesson4_Task2.primes_era(3)" 1000 loops, best of 5: 1.08 usec per loop
#  "GB_Algorithm_Lesson4_Task2.primes_era(10)" 1000 loops, best of 5: 10.3 usec per loop
#  "GB_Algorithm_Lesson4_Task2.primes_era(100)" 1000 loops, best of 5: 1.45 msec per loop

cProfile.run('primes_era(100)')

#  GB_Algorithm_Lesson4_Task2.py 20 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task2.py 192 function calls in 0.000 seconds
#  GB_Algorithm_Lesson4_Task2.py 21656 function calls in 0.003 seconds

# алгоритм Эратосфена не самый оптимальный, особенно на больших массивах

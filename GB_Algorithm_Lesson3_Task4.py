"""
Задача 4.
Определить, какое число в массиве встречается чаще всего.
"""

import random

size = 10
my_array = [random.randint(-10, 10) for _ in range(size)]
print(my_array)

freq_meet = None
num_freq_meet = 0

for item in my_array:
    num = my_array.count(item)
    if num > num_freq_meet:
        num_freq_meet = num
        freq_meet = item

print(freq_meet)  # первое из одинаково много встречающихся

"""
Задача 4.
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов n: '))
a = 1
res = 0
while n != 0:
    res += a
    a /= (-2)
    n -= 1
print('сумма элементов равна ', res)
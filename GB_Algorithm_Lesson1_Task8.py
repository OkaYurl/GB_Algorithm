"""
Задача 8.
Вводятся три разных числа. Найти, какое из них является
средним (больше одного, но меньше другого).
"""

a, b, c = input("Введите три разных числа a b c через пробел: ").split()
a, b, c = int(a), int(b), int(c)  # перевод введенных строк в числовые значения

if a != b and b != c and a != c:
    if b < a < c or c < a < b:
        print(a)
    else:
        if a < b < c or c < b < a:
            print(b)
        else:
            print(c)
else:
    print('Числа должны быть разными.')

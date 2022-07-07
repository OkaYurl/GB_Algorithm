"""
Задача 9.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""

num = int(input('Введите натуральное число (0 для стоп): '))
max_num = 0
max_sum = 0
while num != 0:
    mnum = num
    snum = 0
    while num > 0:
        snum += num % 10
        num //= 10
    if snum > max_sum:
        max_sum = snum
        max_num = mnum
    num = int(input('Введите натуральное число (0 для стоп): '))
print(f'Число {max_num} имеет максимальную сумму цифр {max_sum}')

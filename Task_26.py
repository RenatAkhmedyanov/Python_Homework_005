# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

A = float(input('Введите число: '))
B = int(input('Введите степень числа: '))

def degree(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * degree(a, b - 1)
    else:
        return 1 / a * degree(1 / a, abs(b) - 1)             

result = degree(A, B)
print(f'{A} в степени {B} = {result}')
# 2) Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def f(n):
    ls = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ls.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ls.append(n)
    return ls


print(f(int(input('Input a natural number: '))))

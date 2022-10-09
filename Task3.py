#  3) Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

data = list(map(int, '6 7 8 9 9 7 5 4 3 2'.split()))
print(data)
res = list(filter(lambda x: data.count(x) == 1, data))
print(res)

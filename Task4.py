# 4) Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

data = list(map(str, 'qwe asd zxc qwe ert qwe'.split()))
print(data)


def pos2(x, y: list):
    if x in y and y.count(x) > 1:
        pos1 = y.index(x)
        print(f' The second occurrencey has {y.index(x, pos1 + 1)} index')
    else:
        print('There are not second occurrence.')


pos2(input('Input the word to find the second occurrence: '), data)

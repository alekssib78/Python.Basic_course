# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдуще
# го, например:
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
# Подсказка: использовать возможности python, изученные на уроке.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def greated_num():
    a=src[0]
    result = []
    for i in src:
        if i > a:
            result.append(i)
            a = i
        else:
            a = i
    yield result

res = greated_num()
print(*res)

great_num = [src[i] for i in range(1, len(src))
    if src[i - 1] < src[i]]
print(great_num)





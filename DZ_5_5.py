# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с
# сохранением порядка их следования в исходном списке, например:
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
from time import perf_counter
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = []
for i in src:
    if src.count(i) == 1:
        result.append(i)
print(result, perf_counter() - start)


start = perf_counter()
result_gen = [i for i in src if src.count(i)==1]
print(result_gen, perf_counter() - start)


start = perf_counter()
uniq_src = set()
tmp = set()
for i in src:
    if i not in tmp:
        uniq_src.add(i)
    else:
        uniq_src.discard(i)
    tmp.add(i)
print(uniq_src, perf_counter() - start)
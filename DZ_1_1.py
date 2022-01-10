#      Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах:
#
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.
while True:
    duration = int(input('Введите период в секундах :'))
#  первое условие задания значение до минуты
    seconds = duration % 60         # остаток от деления выведет секунды
    duration = duration // 60       # целочисленным делением на 60 убираем значение секунд, остаются минуты
    minutes = duration % 60         # остаток от деления выведет минуты
#  второе условие задания до часа до суток
    duration = duration // 60       # остаются часы
    hours = duration % 24           # выведет часы
    duration = duration // 24       # остаются дни
    day = duration             # выведет дни
    if day > 0:
        print(f'{day} день(дней) {hours} час {minutes} мин {seconds} сек')
    elif day == 0 and hours > 0:
        print(f'{hours} час {minutes} мин {seconds} сек')
    elif hours == 0 and minutes > 0:
        print(f' {minutes} мин {seconds} сек')
    else:
        print(f' {seconds} сек')


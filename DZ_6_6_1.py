#  Для чтения данных реализовать в
# командной строке следующую логику:
#
#     просто запуск скрипта — выводить все записи;
#     запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу,
# до конца;
#     запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по
# номер, равный второму числу, включительно.
#
#  Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
#
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры
# запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
import sys
def show_sales():

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        # выводит файл полностью
        if len(sys.argv) == 1:
            show_full = f.read()
            return print(show_full)
        else:
            show = f.readlines()
            if len(sys.argv) == 2:
                num_start = int(sys.argv[1]) - 1
                return print(*show[num_start:])
            else:
                num_start = int(sys.argv[1]) - 1
                num_end = int(sys.argv[2])
                return print(*show[num_start:num_end])

show_sales()



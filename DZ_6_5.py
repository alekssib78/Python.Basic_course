# 5.**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных
#  файлов и имя выходного файла. Проверить работу скрипта.
from itertools import zip_longest

import sys


def create_file():

    with open(sys.argv[1], 'r', encoding='utf-8') as user,\
        open(sys.argv[2], 'r', encoding='utf-8') as hobby,\
        open(sys.argv[3],'w', encoding='utf-8') as uh_txt:
        for line, value in zip_longest(user, hobby):
            value = value.strip()
            if line is not None:

                line = line.replace(',', ' ').strip()  # если имя имеется то вырезаем запятые и знаки переноса
                if value != '':
                    print('хоби имеется')
                    print(line, value)  # если хобби имеется печатаем имя хобби
                    uh_txt.write(f'{line}: {value} \n')
                else:
                    print('хобби закончилось')
                    value = None  # если хобби закончилось,хобби = None
                    print(line, value)
                    uh_txt.write(f'{line}: {value} \n')
            else:
                print('ФИО закончилось')  # если закончились ФИО выходим с кодом 1

                return exit(1)

print('hello')

if __name__ == '__main__':
    print(create_file())

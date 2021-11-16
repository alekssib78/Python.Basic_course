# 4.*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не
# нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
from itertools import zip_longest

def create_file():

    with open('users.csv', 'r', encoding='utf-8') as user,\
        open('hobby.csv', 'r', encoding='utf-8') as hobby,\
        open('users_hobby.txt','w',encoding='utf-8') as uh_txt:
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

print(create_file())



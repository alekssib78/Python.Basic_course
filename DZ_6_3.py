# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в
# файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
# считать, что объём данных в файлах во много раз меньше объема ОЗУ. Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

from itertools import zip_longest

def creted_dict():
    creted_dict_file = dict()

    with open('users.csv', 'r', encoding='utf-8') as key, \
            open('hobby.csv', 'r', encoding='utf-8') as value, \
            open('create_dict.txt', 'w', encoding='utf-8') as creat_dict_fi:  # открываем файлы на чтение и оди для записи

        for str_key, str_value in zip_longest(key, value):

            str_value = str_value.strip()  # вырезаем скрытые символы
            if str_key is not None:  # если ключ не равен None
                if str_value != '':  # и если значения не пустые кавычки
                    str_key = str_key.replace(',', ' ').strip() # вырезаем запятые и скрытые символы
                    creted_dict_file.setdefault(str_key,str_value) # записываем строку в файл

                else:  # если нет значения
                    str_value = 'None'
                    creted_dict_file.setdefault(str_key, str_value)
                print(creted_dict_file)

            elif str_key is None and str_value == '': # если закончились ключи и значения выходим с кодом 0
                exit()
            else:
                exit(1) # если закончились ключи выходим с кодом 1


print(creted_dict())






















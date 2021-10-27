# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
# задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
# функции currency_rates(). Убедиться, что ничего лишнего не происходит.


from requests import get
from requests import utils
from decimal import *
from datetime import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(charcode):

    charcode = charcode.upper()
    if charcode in content:
        charcode_spot = (content.find(f'{charcode}'))  # индекс начала кода валюты
        valute = content[charcode_spot:charcode_spot + 3]  # выводим код валюты
        nominal_start = content.find('<Nominal>', charcode_spot) + 9  # находим начало суммы номинала
        nominal_end = content.find('</Nominal>', charcode_spot)  # находим окончание суммы номинала
        nominal = content[nominal_start:nominal_end]  # выводим номинал выбранной валюты
        name_start = content.find('<Name>', charcode_spot) + 6  # начало названия валюты
        name_end = content.find('</Name>', charcode_spot)  # конец названия валюты
        name = content[name_start:name_end]  # название валюты
        value_start = content.find('<Value>', charcode_spot) + 7  # начало значения
        value_end = content.find('</Value>', charcode_spot)  # конец значения
        value_str = content[value_start:value_end]  # находим курс
        value_list = value_str.split(',')  # создаем список из строк разделитель запятая между числами
        value = '.'.join(value_list)  # соединяем цифры в списке через точку
        value_float = float(value)  # преобразуем строку в float
        value_decimal = Decimal(value)  # преобразуем строку в Decimal
        date_start = content.find('Date="') + 6
        date_end = content.find('" name="Foreign')
        date_str = content[date_start:date_end]
        date_format = datetime.strptime(date_str, '%d.%m.%Y').date()  # если убрать в конце date(),выведет дату и время
        return print(f'На "{date_format}" <<{nominal}>> {name} {valute}= <<{value_decimal}>> рублей')


    else:
        return print('None')






if __name__ == '__main__':
    currency_rates('usd')
    currency_rates('eur')
    currency_rates('try')
    currency_rates('rere')







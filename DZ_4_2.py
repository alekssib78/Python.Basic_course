#  2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.

from requests import get
from requests import utils
from decimal import Decimal

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

        print(f'<<{nominal}>> {name} {valute} = <<{value_float}>> рублей')
        print(f'<<{nominal}>> {name} {valute}= <<{value_decimal}>> рублей')

    else:
        print('None')







currency_rates('usd')
currency_rates('eur')
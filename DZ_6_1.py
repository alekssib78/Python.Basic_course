# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
#
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

import requests

log_file_url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
log_file_name = "nginx_logs.txt"

remote_addr = 0
request_type = 5
requested_resource = 6
moder_nginx = []

response = requests.get(log_file_url,stream=True) # разрешаем загружать частями

with open(log_file_name, 'wb') as f:  # Записываем в файл
    for chunk in response.iter_content(chunk_size= 1024): # назначаем размер скачиваемых фрагментов
        f.write(chunk) # записываем фрагменты

with open(log_file_name, 'r') as f:

    for line in f:

        if line.find('product_2') != -1:  # выбрали строки в которых встречается нужное значение
            bit = line.split()  # разбиваем строку по пробелам
            requests_type = bit[request_type] #
            correct_request_type = requests_type.strip('"') # удаляем ковычки
            tuple_bit = (bit[remote_addr], correct_request_type , bit[requested_resource]) # создаем кортеж на вывод

            moder_nginx.append(tuple_bit)  # добавляем кортежи в список


print(moder_nginx)










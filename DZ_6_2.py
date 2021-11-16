# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.

import requests

log_file_url = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
log_file_name = "nginx_logs.txt"


remote_addr = 0

moder_nginx = []

response = requests.get(log_file_url,stream=True) # разрешаем загружать частями

with open(log_file_name, 'wb') as f:  # Записываем в файл
    for chunk in response.iter_content(chunk_size= 1024): # назначаем размер скачиваемых фрагментов
        f.write(chunk) # записываем фрагменты

with open(log_file_name, 'r') as f:

    for line in f:
        bit = line.split()  # разбиваем строку по пробелам
        tuple_bit = bit[remote_addr]  # находим адрес откуда поступал запрос
        moder_nginx.append(tuple_bit) # добавляем в список адрес запроса
result = dict((i,moder_nginx.count(i)) for i in moder_nginx)
spam = result
print(max(result.items(), key = lambda x: x[1]))


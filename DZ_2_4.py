#     Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
#  'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
# 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к
# корректному виду. Можно ли при этом не создавать новый список?
staff_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
print(staff_list)
print(id(staff_list))

for i in staff_list:
    name = (f"Привет, {i.split(' ')[-1]}!")  # для каждой строки списка выбираем последнее значение которое по условию
    # имя
    print(name.title())  # первую букву переводим в заглавную остальные маленькие

for i in staff_list:
    u = staff_list.index(i)
    g = i.split(' ')  # разбиваем строку по пробелам
    staff_list.pop(u)  # удаляем строку по индексу
    staff_list.insert(u, i.replace(g[-1], g[-1].title()))  # вставляем вместо удаленной строки свои значения
print(staff_list)
print(id(staff_list))
